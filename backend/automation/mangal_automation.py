"""
GARUDA POWER — MANGAL (EXPIRY SCALP GROUP) Automation Engine
==============================================================
यह एक ही स्क्रिप्ट है जो Mangal पेज के सभी 6 बॉक्स चलाती है:

  1. pcr            -> PCR Sentiment
  2. greeksscalp    -> Options Greeks Scalp (आपका दिया formula)
  3. vwapscalp      -> VWAP Mean-Reversion
  4. oibuildup      -> OI Buildup Tracker
  5. momentumscalp  -> Price Momentum Scalp
  6. orbscalp       -> Opening Range Breakout

हर बॉक्स का अपना "मूल मंत्र" (scoring formula) नीचे अलग function में है।
हर बार चलने पर:
  - 6 scores calculate होते हैं
  - garuda_live_data.json में लिखे जाते हैं (HTML इसे पढ़ती है)
  - garuda_mangal_history.csv में Pandas के through history भी save होती है
    (यह history आगे "Summary" पेज में signals/target/SL गिनने के लिए use होगी)

==================================================================
🔌 असली डेटा कनेक्ट करने के लिए सिर्फ "fetch_*_inputs()" functions
   के अंदर अपने broker API calls डालें — बाकी सब वैसा ही चलेगा।
==================================================================
"""

import json
import time
import os
from datetime import datetime

import pandas as pd

# ----------------------------------------------------------------
# CONFIG
# ----------------------------------------------------------------
OUTPUT_FILE   = "garuda_live_data.json"
HISTORY_FILE  = "garuda_mangal_history.csv"
SCAN_INTERVAL = 15   # seconds

BUY_THRESHOLD  = 70
SELL_THRESHOLD = 35


# ==================================================================
# 1) PCR SENTIMENT  ->  id: 'pcr'
# ==================================================================
def fetch_pcr_inputs():
    """
    🔌 असली डेटा: broker के option-chain से कुल Put OI / Call OI निकालकर
    PCR = Put OI / Call OI calculate करें, फिर 0-100 में normalize करें।
    अभी placeholder values हैं।
    """
    return {
        "pcr_bullish_score":  68,   # PCR कितना bullish zone में है (0-100)
        "pcr_trend_strength": 60,   # PCR trend कितना मजबूत हो रहा है (0-100)
        "oi_support_score":   72,   # OI support level से alignment (0-100)
    }

def score_pcr(i):
    """मूल मंत्र: PCR Sentiment Score"""
    score = (
        i["pcr_bullish_score"]  * 0.50 +
        i["pcr_trend_strength"] * 0.30 +
        i["oi_support_score"]   * 0.20
    )
    return round(score, 2)

def criteria_pcr(i, score):
    return [
        {"label": f"PCR bullish zone (score {i['pcr_bullish_score']})",        "pass": i["pcr_bullish_score"]  >= 55},
        {"label": f"PCR trend strengthening (score {i['pcr_trend_strength']})","pass": i["pcr_trend_strength"] >= 55},
        {"label": f"OI support alignment (score {i['oi_support_score']})",     "pass": i["oi_support_score"]   >= 55},
        {"label": "No sudden PCR reversal (last 3 candles)",                   "pass": True},
    ]


# ==================================================================
# 2) OPTIONS GREEKS SCALP  ->  id: 'greeksscalp'   (आपका दिया formula)
# ==================================================================
def fetch_greeks_inputs():
    """
    🔌 असली डेटा: ATM CE/PE का Gamma, Delta, Volume, OI strength, Theta —
    सब broker option-chain API से 0-100 normalize करके भरें।
    """
    return {
        "confidence":    90,
        "gamma":         85,
        "delta":         80,
        "volume":        88,
        "oi_strength":   82,
        "theta_penalty": 30,
    }

def score_greeks(i):
    """मूल मंत्र: Scalp Quality Score (आपका formula)"""
    score = (
        i["confidence"]    * 0.30 +
        i["gamma"]         * 0.20 +
        i["delta"]         * 0.15 +
        i["volume"]        * 0.15 +
        i["oi_strength"]   * 0.10 -
        i["theta_penalty"] * 0.10
    )
    return round(score, 2)

def criteria_greeks(i, score):
    return [
        {"label": f"Confidence ≥ 70 (अभी {i['confidence']})",       "pass": i["confidence"]    >= 70},
        {"label": f"Gamma strong ≥ 60 (अभी {i['gamma']})",          "pass": i["gamma"]         >= 60},
        {"label": f"Delta aligned ≥ 50 (अभी {i['delta']})",         "pass": i["delta"]         >= 50},
        {"label": f"Volume active ≥ 50 (अभी {i['volume']})",        "pass": i["volume"]        >= 50},
        {"label": f"OI build-up ≥ 50 (अभी {i['oi_strength']})",     "pass": i["oi_strength"]   >= 50},
        {"label": f"Theta penalty ≤ 40 (अभी {i['theta_penalty']})", "pass": i["theta_penalty"] <= 40},
    ]


# ==================================================================
# 3) VWAP MEAN-REVERSION  ->  id: 'vwapscalp'
# ==================================================================
def fetch_vwap_inputs():
    """
    🔌 असली डेटा: price का VWAP से distance (%), RSI value, reversal
    candle की strength, और volume confirmation — सब 0-100 normalize करें।
    """
    return {
        "vwap_distance_score": 74,
        "rsi_reversal_score":  66,
        "candle_strength":     70,
        "volume_confirm":      62,
    }

def score_vwap(i):
    """मूल मंत्र: VWAP Mean-Reversion Score"""
    score = (
        i["vwap_distance_score"] * 0.35 +
        i["rsi_reversal_score"]  * 0.25 +
        i["candle_strength"]     * 0.25 +
        i["volume_confirm"]      * 0.15
    )
    return round(score, 2)

def criteria_vwap(i, score):
    return [
        {"label": f"Price away from VWAP (score {i['vwap_distance_score']})", "pass": i["vwap_distance_score"] >= 55},
        {"label": f"RSI confirms reversal (score {i['rsi_reversal_score']})", "pass": i["rsi_reversal_score"]  >= 55},
        {"label": f"Strong reversal candle (score {i['candle_strength']})",   "pass": i["candle_strength"]     >= 55},
        {"label": f"Volume confirms move (score {i['volume_confirm']})",      "pass": i["volume_confirm"]      >= 55},
    ]


# ==================================================================
# 4) OI BUILDUP TRACKER  ->  id: 'oibuildup'
# ==================================================================
def fetch_oi_inputs():
    """
    🔌 असली डेटा: strike-wise OI change % (vs पिछले snapshot), price-OI
    correlation, OI concentration, volume support — 0-100 normalize करें।
    """
    return {
        "oi_change_score":        78,
        "price_oi_correlation":   71,
        "strike_concentration":   65,
        "volume_support":         69,
    }

def score_oi(i):
    """मूल मंत्र: OI Buildup Score"""
    score = (
        i["oi_change_score"]      * 0.35 +
        i["price_oi_correlation"] * 0.30 +
        i["strike_concentration"] * 0.20 +
        i["volume_support"]       * 0.15
    )
    return round(score, 2)

def criteria_oi(i, score):
    return [
        {"label": f"Significant OI change (score {i['oi_change_score']})",       "pass": i["oi_change_score"]      >= 55},
        {"label": f"Price-OI relation confirms (score {i['price_oi_correlation']})","pass": i["price_oi_correlation"] >= 55},
        {"label": f"OI concentration at key strikes (score {i['strike_concentration']})","pass": i["strike_concentration"] >= 55},
        {"label": f"Volume supports OI buildup (score {i['volume_support']})",   "pass": i["volume_support"]       >= 55},
    ]


# ==================================================================
# 5) PRICE MOMENTUM SCALP  ->  id: 'momentumscalp'
# ==================================================================
def fetch_momentum_inputs():
    """
    🔌 असली डेटा: 1-min candle range burst, 5/13 EMA alignment, RSI
    momentum, volume spike — सब 0-100 normalize करें।
    """
    return {
        "candle_burst_score":  73,
        "ema_alignment_score": 68,
        "rsi_momentum":        64,
        "volume_spike":        70,
    }

def score_momentum(i):
    """मूल मंत्र: Price Momentum Scalp Score"""
    score = (
        i["candle_burst_score"]  * 0.30 +
        i["ema_alignment_score"] * 0.25 +
        i["rsi_momentum"]        * 0.25 +
        i["volume_spike"]        * 0.20
    )
    return round(score, 2)

def criteria_momentum(i, score):
    return [
        {"label": f"Candle range burst (score {i['candle_burst_score']})",   "pass": i["candle_burst_score"]  >= 55},
        {"label": f"5/13 EMA aligned (score {i['ema_alignment_score']})",    "pass": i["ema_alignment_score"] >= 55},
        {"label": f"RSI momentum confirms (score {i['rsi_momentum']})",      "pass": i["rsi_momentum"]         >= 55},
        {"label": f"Volume spike on burst (score {i['volume_spike']})",      "pass": i["volume_spike"]         >= 55},
    ]


# ==================================================================
# 6) OPENING RANGE BREAKOUT  ->  id: 'orbscalp'
# ==================================================================
def fetch_orb_inputs():
    """
    🔌 असली डेटा: opening range breakout strength, retest hold, higher
    timeframe trend alignment, breakout volume — 0-100 normalize करें।
    """
    return {
        "breakout_strength":     75,
        "retest_hold_score":     60,
        "htf_trend_alignment":   80,
        "volume_on_breakout":    77,
    }

def score_orb(i):
    """मूल मंत्र: Opening Range Breakout Score"""
    score = (
        i["breakout_strength"]   * 0.35 +
        i["retest_hold_score"]   * 0.20 +
        i["htf_trend_alignment"] * 0.25 +
        i["volume_on_breakout"]  * 0.20
    )
    return round(score, 2)

def criteria_orb(i, score):
    return [
        {"label": f"Breaks opening range (score {i['breakout_strength']})",     "pass": i["breakout_strength"]   >= 55},
        {"label": f"Retest holds level (score {i['retest_hold_score']})",       "pass": i["retest_hold_score"]   >= 55},
        {"label": f"HTF trend aligned (score {i['htf_trend_alignment']})",      "pass": i["htf_trend_alignment"] >= 55},
        {"label": f"Volume on breakout (score {i['volume_on_breakout']})",      "pass": i["volume_on_breakout"]  >= 55},
    ]


# ==================================================================
# COMMON — status decision
# ==================================================================
def decide_status(score):
    if score >= BUY_THRESHOLD:
        return "BUY"
    if score <= SELL_THRESHOLD:
        return "SELL"
    return "WAIT"


# ==================================================================
# REGISTRY — सभी 6 बॉक्स एक जगह
# ==================================================================
BOXES = {
    "pcr":           (fetch_pcr_inputs,       score_pcr,       criteria_pcr),
    "greeksscalp":   (fetch_greeks_inputs,    score_greeks,    criteria_greeks),
    "vwapscalp":     (fetch_vwap_inputs,      score_vwap,      criteria_vwap),
    "oibuildup":     (fetch_oi_inputs,        score_oi,        criteria_oi),
    "momentumscalp": (fetch_momentum_inputs,  score_momentum,  criteria_momentum),
    "orbscalp":      (fetch_orb_inputs,       score_orb,       criteria_orb),
}


# ==================================================================
# RUN ONCE — सभी 6 calculate, JSON लिखो, Pandas history save करो
# ==================================================================
def run_once():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    json_data = {}
    history_row = {"timestamp": timestamp}

    for box_id, (fetch_fn, score_fn, criteria_fn) in BOXES.items():
        inputs = fetch_fn()
        score = score_fn(inputs)
        status = decide_status(score)
        confidence = inputs.get("confidence", int(score))

        json_data[box_id] = {
            "status":     status,
            "score":      int(score),
            "confidence": int(confidence),
            "criteria":   criteria_fn(inputs, score),
        }

        history_row[f"{box_id}_score"]  = score
        history_row[f"{box_id}_status"] = status

    # ---- 1) HTML के लिए JSON ----
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)

    # ---- 2) Pandas history (CSV) ----
    df_row = pd.DataFrame([history_row])
    if os.path.exists(HISTORY_FILE):
        df_row.to_csv(HISTORY_FILE, mode="a", header=False, index=False)
    else:
        df_row.to_csv(HISTORY_FILE, mode="w", header=True, index=False)

    # ---- 3) Console summary ----
    line = "  ".join(f"{bid}={json_data[bid]['status']}({json_data[bid]['score']})" for bid in BOXES)
    print(f"[{timestamp}]  {line}")


# ==================================================================
# MAIN LOOP — Digital Ocean सर्वर पर background में हमेशा चलेगा
# ==================================================================
if __name__ == "__main__":
    print(f"🦅 GARUDA — MANGAL (Expiry Scalp Group) Automation शुरू — हर {SCAN_INTERVAL} सेकंड")
    print(f"   -> {OUTPUT_FILE}  (HTML यहाँ से live update लेगी)")
    print(f"   -> {HISTORY_FILE} (Pandas history — आगे Summary पेज के लिए)")
    while True:
        try:
            run_once()
        except Exception as e:
            print("⚠️ Error:", e)
        time.sleep(SCAN_INTERVAL)
