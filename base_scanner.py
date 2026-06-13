# scanners/base_scanner.py — सभी scanners का base class
import pandas as pd
import numpy as np

class BaseScanner:
    """
    सभी 11 scanners इसी से inherit करते हैं।
    हर scanner को सिर्फ scan() method implement करना है।
    """

    def __init__(self, name, scanner_id):
        self.name       = name
        self.scanner_id = scanner_id

    def scan(self, data: dict) -> dict:
        """Override this in each scanner"""
        raise NotImplementedError

    # ══════════════════════════════════════
    # SHARED UTILITY FUNCTIONS (Pandas)
    # ══════════════════════════════════════

    def to_df(self, data: dict) -> pd.DataFrame:
        """Dict को DataFrame में बदलो"""
        df = pd.DataFrame({
            'open':   data['open'],
            'high':   data['high'],
            'low':    data['low'],
            'close':  data['close'],
            'volume': data['volume'],
        })
        return df

    def ema(self, series: pd.Series, period: int) -> pd.Series:
        return series.ewm(span=period, adjust=False).mean()

    def rsi(self, series: pd.Series, period: int = 14) -> pd.Series:
        delta = series.diff()
        gain  = delta.clip(lower=0)
        loss  = -delta.clip(upper=0)
        avg_g = gain.ewm(com=period - 1, adjust=False).mean()
        avg_l = loss.ewm(com=period - 1, adjust=False).mean()
        rs    = avg_g / avg_l.replace(0, np.nan)
        return 100 - (100 / (1 + rs))

    def macd(self, series: pd.Series, fast=12, slow=26, signal=9):
        fast_ema   = self.ema(series, fast)
        slow_ema   = self.ema(series, slow)
        macd_line  = fast_ema - slow_ema
        signal_line = self.ema(macd_line, signal)
        histogram  = macd_line - signal_line
        return macd_line, signal_line, histogram

    def bollinger_bands(self, series: pd.Series, period=20, std_dev=2):
        ma    = series.rolling(period).mean()
        std   = series.rolling(period).std()
        upper = ma + std_dev * std
        lower = ma - std_dev * std
        return upper, ma, lower

    def atr(self, df: pd.DataFrame, period=14) -> pd.Series:
        tr = pd.concat([
            df['high'] - df['low'],
            (df['high'] - df['close'].shift()).abs(),
            (df['low']  - df['close'].shift()).abs()
        ], axis=1).max(axis=1)
        return tr.rolling(period).mean()

    def obv(self, df: pd.DataFrame) -> pd.Series:
        direction = df['close'].diff().apply(lambda x: 1 if x > 0 else (-1 if x < 0 else 0))
        return (direction * df['volume']).cumsum()

    def vwap(self, df: pd.DataFrame) -> pd.Series:
        tp = (df['high'] + df['low'] + df['close']) / 3
        return (tp * df['volume']).cumsum() / df['volume'].cumsum()

    def stochastic(self, df: pd.DataFrame, k=14, d=3):
        low_min  = df['low'].rolling(k).min()
        high_max = df['high'].rolling(k).max()
        k_line   = 100 * (df['close'] - low_min) / (high_max - low_min + 1e-10)
        d_line   = k_line.rolling(d).mean()
        return k_line, d_line

    def build_result(self, scanner_id, signal, score, max_score,
                     conditions, price, t1, t2, t3, sl,
                     strength=None, extra=None):
        """Standard result format"""
        return {
            'id':       scanner_id,
            'signal':   signal,        # BUY / SELL / NO_SIGNAL
            'strength': strength or ('STRONG' if score / max_score >= 0.8 else 'MODERATE'),
            'score':    score,
            'maxScore': max_score,
            'conditions': conditions,  # list of {name, passed}
            'price': round(price, 2),
            't1':    round(t1, 2),
            't2':    round(t2, 2),
            't3':    round(t3, 2),
            'sl':    round(sl, 2),
            'extra': extra or {}
        }
