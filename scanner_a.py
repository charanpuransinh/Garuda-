# scanners/scanner_a.py — Pattern Scanner (EMA + RSI + MACD)
from .base_scanner import BaseScanner
import numpy as np

class ScannerA(BaseScanner):
    def __init__(self):
        super().__init__("PATTERN SCANNER", "A")

    def scan(self, data: dict) -> dict:
        df = self.to_df(data)
        if len(df) < 50:
            return {'id': 'A', 'signal': 'NO_SIGNAL', 'score': 0, 'maxScore': 8, 'conditions': []}

        close = df['close']
        price = close.iloc[-1]
        atr_v = self.atr(df).iloc[-1] or price * 0.01

        # === CONDITIONS ===
        ema9  = self.ema(close, 9)
        ema21 = self.ema(close, 21)
        ema50 = self.ema(close, 50)

        c1 = bool(close.iloc[-1] > ema9.iloc[-1] > ema21.iloc[-1] > ema50.iloc[-1])

        rsi_val = self.rsi(close).iloc[-1]
        c2 = bool(45 < rsi_val < 70)

        macd_l, macd_s, macd_h = self.macd(close)
        c3 = bool(macd_h.iloc[-1] > 0 and macd_h.iloc[-2] <= 0)  # Fresh crossover

        upper_bb, mid_bb, lower_bb = self.bollinger_bands(close)
        c4 = bool(close.iloc[-1] > mid_bb.iloc[-1])

        vol_ma = df['volume'].rolling(20).mean()
        c5 = bool(df['volume'].iloc[-1] > vol_ma.iloc[-1] * 1.5)

        # Higher High + Higher Low (last 10 bars)
        recent_highs = df['high'].iloc[-10:]
        c6 = bool(recent_highs.iloc[-1] > recent_highs.iloc[0])

        # Strong bullish candle
        body  = abs(close.iloc[-1] - df['open'].iloc[-1])
        range_= df['high'].iloc[-1] - df['low'].iloc[-1]
        c7 = bool(range_ > 0 and body / range_ > 0.6)

        obv_val = self.obv(df)
        c8 = bool(obv_val.iloc[-1] > obv_val.iloc[-5])

        conditions = [
            {'name': 'EMA Stack 9>21>50',      'passed': c1},
            {'name': 'RSI Healthy 45-70',       'passed': c2},
            {'name': 'MACD Fresh Crossover',    'passed': c3},
            {'name': 'Price > BB Midline',      'passed': c4},
            {'name': 'Volume Surge 1.5x',       'passed': c5},
            {'name': 'Higher High Pattern',     'passed': c6},
            {'name': 'Strong Bull Candle >60%', 'passed': c7},
            {'name': 'OBV Uptrend 5-bar',       'passed': c8},
        ]

        score    = sum(1 for c in conditions if c['passed'])
        max_score = 8

        if score >= 6:
            return self.build_result(
                'A', 'BUY', score, max_score, conditions, price,
                t1=price + atr_v * 2,
                t2=price + atr_v * 3.5,
                t3=price + atr_v * 5,
                sl=price - atr_v * 1.2,
                extra={'rsi': round(rsi_val, 1), 'ema9': round(ema9.iloc[-1], 2)}
            )

        return {'id': 'A', 'signal': 'NO_SIGNAL', 'score': score,
                'maxScore': max_score, 'conditions': conditions,
                'price': round(price, 2)}
