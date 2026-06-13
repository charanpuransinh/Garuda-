# run_scanners.py — सभी scanners चलाओ, JSON output दो
# server.js इसे call करता है

import sys
import json
import time
from datetime import datetime

# Angel One API
try:
    from angel_api import AngelOneAPI, DEFAULT_SYMBOLS
    USE_LIVE_DATA = True
except Exception as e:
    USE_LIVE_DATA = False
    print(f"Warning: Live API not available: {e}", file=sys.stderr)

# All scanners import
from scanners.scanner_a import ScannerA
from scanners.scanner_b import ScannerB
from scanners.scanner_c import ScannerC
from scanners.scanner_d import ScannerD
from scanners.scanner_e import ScannerE
from scanners.scanner_f import ScannerF
from scanners.scanner_g import ScannerG
from scanners.scanner_h import ScannerH
from scanners.scanner_i import ScannerI
from scanners.scanner_j import ScannerJ
from scanners.scanner_k import ScannerK

# ══════════════════════════════════════════
# SCANNERS LIST
# ══════════════════════════════════════════
SCANNERS = {
    'A': ScannerA,
    'B': ScannerB,
    'C': ScannerC,
    'D': ScannerD,
    'E': ScannerE,
    'F': ScannerF,
    'G': ScannerG,
    'H': ScannerH,
    'I': ScannerI,
    'J': ScannerJ,
    'K': ScannerK,
}

def get_data(symbol):
    """Angel One se ya demo data lo"""
    if USE_LIVE_DATA:
        try:
            api = AngelOneAPI()
            if api.login():
                return api.get_ohlcv(symbol, interval="FIVE_MINUTE", days=5)
        except Exception as e:
            print(f"Live data failed, using demo: {e}", file=sys.stderr)

    # Demo data fallback
    return generate_demo_data(symbol)

def generate_demo_data(symbol, candles=100):
    """Demo OHLCV data"""
    import random
    import math
    prices = [1000.0]
    for i in range(candles - 1):
        change = random.gauss(0, 0.012)
        prices.append(round(prices[-1] * (1 + change), 2))

    opens  = prices
    closes = [p * (1 + random.gauss(0, 0.004)) for p in prices]
    highs  = [max(o, c) * (1 + abs(random.gauss(0, 0.005))) for o, c in zip(opens, closes)]
    lows   = [min(o, c) * (1 - abs(random.gauss(0, 0.005))) for o, c in zip(opens, closes)]
    vols   = [random.randint(50000, 500000) for _ in prices]

    return {
        'symbol': symbol,
        'open':   opens,
        'high':   highs,
        'low':    lows,
        'close':  closes,
        'volume': vols,
    }

def run_all(symbol):
    """सभी scanners चलाओ"""
    data = get_data(symbol)
    if not data:
        print(json.dumps({'error': 'No data', 'symbol': symbol}))
        return

    results = {
        'symbol':    symbol,
        'timestamp': datetime.now().isoformat(),
        'scanners':  {}
    }

    buy_count  = 0
    sell_count = 0
    wait_count = 0

    for key, ScannerClass in SCANNERS.items():
        try:
            scanner = ScannerClass()
            result  = scanner.scan(data)

            results['scanners'][key] = result

            sig = result.get('signal', 'NO_SIGNAL')
            if sig == 'BUY':
                buy_count += 1
            elif sig == 'SELL':
                sell_count += 1
            else:
                wait_count += 1

        except Exception as e:
            results['scanners'][key] = {
                'signal': 'ERROR',
                'error':  str(e),
                'score':  0,
                'maxScore': 10
            }

    results['summary'] = {
        'buy':   buy_count,
        'sell':  sell_count,
        'wait':  wait_count,
        'total': len(SCANNERS),
        'consensus': 'BULLISH' if buy_count > sell_count else
                     'BEARISH' if sell_count > buy_count else 'NEUTRAL'
    }

    # JSON output — server.js yahi padhega
    print(json.dumps(results))

# ══════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════
if __name__ == "__main__":
    symbol = sys.argv[1] if len(sys.argv) > 1 else "RELIANCE"
    run_all(symbol)
