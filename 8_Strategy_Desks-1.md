# Scanner — 8 Strategies (Har Ek Apna Alag Desk/Page)

Har desk ka fixed pattern: **3 OLD (proven) + 2 NEW (2022-2026 generation) indicators + ATR (volatility/stop) + Fibonacci Pivot (Support/Resistance, common across all desks)**

Common 8-step status check (Index Green, Sector Green, Momentum, Volume, Breakout, S/R, Candlestick) sab desks par overlay hoga.

---

## DESK 1 — Indicator Based Strategy

| Type | Indicator | Accuracy (1-10) | Reasoning |
|---|---|---|---|
| OLD 1 | ADX | 7 | Trend strength batata hai, direction nahi — filter ke roop mein use |
| OLD 2 | RSI / Connors RSI | 7.5 | Momentum confirm — Connors RSI(3) zyada precise |
| OLD 3 | SuperTrend | 8 | ATR-based direction + trailing stop, combo ka backbone |
| NEW 1 | ML Adaptive SuperTrend (2024) | 8 | K-Means clustering se volatility regime detect karke SuperTrend adapt karta hai — false signals kam |
| NEW 2 | RSI Velocity/Speedometer (2020) | 7.5 | Momentum ki "speed" measure karta hai — early entry signal |
| ATR | ATR (Average True Range) | 8 | Stop-loss aur volatility-based position sizing |
| S/R | Fibonacci Pivot (PP/R1-R3/S1-S3) | 7 | Mathematical S/R levels — entry/exit zones |

**Combo Accuracy:** ~8.5/10 — ADX (trend hai?) + SuperTrend/ML SuperTrend (direction+stop, dono regime-adaptive) + RSI/RSI Velocity (momentum + speed) → 4 layers. ATR risk control, Fib Pivot entry/exit zones.

**Logic:** ADX > 20-25 + SuperTrend & ML Adaptive SuperTrend same direction + RSI/RSI Velocity momentum confirm + price Fibonacci Pivot level ke paas → Entry. ATR se stop-loss set.

---

## DESK 2 — Price Action Strategy

| Type | Indicator | Accuracy (1-10) | Reasoning |
|---|---|---|---|
| OLD 1 | Support/Resistance (Anchored VWAP) | 8 | Institutional reference price — sabse reliable level |
| OLD 2 | Trendline | 6.5 | Direction confirmation, subjective hai isliye secondary |
| OLD 3 | Candlestick Pattern (Engulfing/Hammer) | 7 | Akela weak, par S/R confluence par strong |
| NEW 1 | Order Block Detector (SMC) | 8 | Institutional order zones — modern S/R ka upgrade |
| NEW 2 | Liquidity Sweep Detector (2021) | 7.5 | Stop-hunt ke baad reversal pattern catch karta hai |
| ATR | ATR | 8 | Stop-loss aur candle size validation |
| S/R | Fibonacci Pivot (PP/R1-R3/S1-S3) | 7 | VWAP/Order Block ke saath confluence → double confirmation |

**Combo Accuracy:** ~8.5/10 — Anchored VWAP + Order Block + Fib Pivot teeno same zone par milein to "triple confluence" — sabse high-probability S/R. Liquidity Sweep stop-hunt confirm karta hai, Candlestick entry timing deta hai.

**Logic:** Price Anchored VWAP/Order Block zone par ho + Fibonacci Pivot level se confluence + Liquidity Sweep (stop hunt) ho chuka ho + Candlestick reversal confirm + Trendline direction match → Entry. ATR se stop-loss.

---

## DESK 3 — Trend Following Strategy

| Type | Indicator | Accuracy (1-10) | Reasoning |
|---|---|---|---|
| OLD 1 | Alpha Trend | 7.5 | Index/Sector trend ke liye ATR-based dynamic trend |
| OLD 2 | Coral Trend | 7 | Smooth color-based trend filter — noise kam |
| OLD 3 | Schaff Trend Cycle | 7 | Faster MACD — early trend signal |
| NEW 1 | AutoTune Filter (Ehlers 2026) | 8.5 | Dominant cycle detect karke adaptive filtering — latest research, sabse high accuracy claim |
| NEW 2 | Precision Trend Analysis (Ehlers 2024) | 8 | Spectral trend separation — trend vs noise alag karta hai |
| ATR | ATR | 8 | Trailing stop trend ke saath |
| S/R | Fibonacci Pivot | 7 | Trend continuation/pullback entry levels |

**Combo Accuracy:** ~8.5/10 — Alpha Trend + Coral Trend (Index+Sector confirm) + AutoTune/Precision Trend (Ehlers latest gen, noise filter) → strong trend confirmation across timeframes. Schaff Trend Cycle early signal deta hai.

**Logic:** Index (Alpha Trend) + Sector (Coral Trend) same direction + AutoTune Filter & Precision Trend Analysis confirm clean trend (not chop) + Schaff Trend Cycle momentum agree + price Fibonacci Pivot pullback level par → Entry. ATR trailing stop.

---

## DESK 4 — Momentum Reversal Strategy

| Type | Indicator | Accuracy (1-10) | Reasoning |
|---|---|---|---|
| OLD 1 | WaveTrend (LazyBear) | 7.5 | Overbought/oversold cross — proven reversal signal |
| OLD 2 | RSI | 7 | Classic momentum confirmation |
| OLD 3 | Fisher Transform | 7 | Price ko Gaussian normal distribution mein convert — sharp turning points |
| NEW 1 | Ultimate Strength Index — USI (Ehlers 2024) | 8 | RSI replacement, less lag — TASC published |
| NEW 2 | Cybernetic Oscillator (Ehlers 2022) | 7.5 | Highpass+lowpass normalized, zero-line cross — clean reversal signal |
| ATR | ATR | 8 | Reversal trade ka stop-loss critical hai |
| S/R | Fibonacci Pivot | 7 | Reversal zone confirmation (price pivot S/R par turn) |

**Combo Accuracy:** ~8.5/10 — WaveTrend + Fisher Transform (dono extreme turning points pakadte hai) + USI (modern RSI, less lag) + Cybernetic Oscillator (noise-free zero cross) → reversal confidence high jab sab agree karein, especially Fibonacci Pivot S/R par.

**Logic:** WaveTrend OB/OS cross + Fisher Transform extreme reading + USI confirms momentum shift + Cybernetic Oscillator zero-line cross + RSI divergence + price Fibonacci Pivot S/R level par reversal → Entry. ATR-based tight stop.

---

## DESK 5 — Mean Reversion Strategy

| Type | Indicator | Accuracy (1-10) | Reasoning |
|---|---|---|---|
| OLD 1 | Connors RSI (CRSI) | 8 | RSI(3)+Streak+PercentRank — mathematically proven mean reversion |
| OLD 2 | Laguerre RSI | 7.5 | 4-pole filter, traditional RSI se kam lag |
| OLD 3 | Hull Suite (Moving Average) | 7 | Reduced-lag MA — mean reversion baseline |
| NEW 1 | David Varadi Oscillator — DVO (2023) | 7.5 | Detrended price, rolling percent rank — quant research backed |
| NEW 2 | Enhanced Andean Oscillator (2025) | 8 | Adaptive envelopes + nonlinear smoothing — latest gen mean reversion |
| ATR | ATR | 8 | Counter-trend trade ka tight stop zaroori |
| S/R | Fibonacci Pivot | 7.5 | Mean reversion entry/exit ke liye exact levels |

**Combo Accuracy:** ~8.5/10 — CRSI + Laguerre RSI + DVO (teeno extreme reading detect karte hai) + Enhanced Andean Oscillator (2025, adaptive bands) → multi-confirmation extreme zone. Hull Suite mean (baseline) deta hai jahan price revert karega. Fib Pivot exact reversal level.

**Logic:** CRSI < 10 / > 90 + Laguerre RSI extreme + DVO percent rank extreme + Enhanced Andean Oscillator band touch + price Hull Suite mean se far + Fibonacci Pivot S/R level par → Entry (counter-trend, tight ATR stop).

---

## DESK 6 — Smart Money Strategy

| Type | Indicator | Accuracy (1-10) | Reasoning |
|---|---|---|---|
| OLD 1 | Order Block Detector (SMC) | 8 | Institutional order blocks — foundation |
| OLD 2 | Fair Value Gap (FVG) | 7.5 | Imbalance zones jo institutions fill karte hai |
| OLD 3 | Liquidity Sweeps | 7.5 | Stop-hunt detection above/below levels |
| NEW 1 | SMC Indicator — LuxAlgo (2022) | 8 | BOS/CHoCH/FVG/OB combined, 800K+ users, institutional grade |
| NEW 2 | Volume Delta / CVD (2020+) | 8 | Tick-level institutional aggression — real buy/sell pressure |
| ATR | ATR | 8 | SMC entries volatile hote hai, ATR stop must |
| S/R | Fibonacci Pivot | 7 | Order Block/FVG ke saath confluence — high probability zone |

**Combo Accuracy:** ~9/10 — Liquidity Sweep (stop hunt) → BOS/CHoCH (SMC LuxAlgo, structure shift confirm) → price FVG/Order Block zone mein return → Volume Delta confirms institutional buying/selling → Fibonacci Pivot confluence. Yeh ek complete institutional footprint sequence hai — sabse high accuracy combo.

**Logic:** Liquidity Sweep (stop hunt) hua + SMC Indicator BOS/CHoCH confirms structure shift + price Order Block/FVG zone + Fibonacci Pivot confluence + Volume Delta/CVD institutional direction confirm → Entry. ATR stop.

---

## DESK 7 — Volume Breakout Strategy

| Type | Indicator | Accuracy (1-10) | Reasoning |
|---|---|---|---|
| OLD 1 | Squeeze Momentum | 7.5 | TTM Squeeze — compression/release breakout timing |
| OLD 2 | Volume Profile (Fixed/Visible) | 7.5 | High-volume node = key breakout level |
| OLD 3 | Cumulative Delta Volume | 7.5 | Buy/sell pressure tracking |
| NEW 1 | SPOTVOL Index (2025, Cboe-listed) | 8 | Spot volatility index — institutional grade, breakout regime confirm |
| NEW 2 | Two-Pole Predictor (2022+) | 7.5 | Predictive price movement, 2-pole filter — early breakout direction |
| ATR | ATR | 8 | Breakout ke baad volatility expansion measure |
| S/R | Fibonacci Pivot | 7.5 | Breakout level = Fib Pivot cross (PP/R1/S1) |

**Combo Accuracy:** ~8.5/10 — Squeeze Momentum (compression) + SPOTVOL (volatility regime confirm, Cboe-listed = institutional grade) + Volume Profile/Delta (real volume confirmation) + Two-Pole Predictor (direction prediction) + Fib Pivot breakout level → high-conviction breakout.

**Logic:** Squeeze Momentum fires (release) + SPOTVOL Index volatility rising + price Volume Profile high-volume node aur Fibonacci Pivot (PP/R1/S1) cross karta hai + Cumulative Delta Volume confirms direction + Two-Pole Predictor agrees → Entry. ATR-based stop/target.

---

## DESK 8 — AI/ML Pattern Strategy

| Type | Indicator | Accuracy (1-10) | Reasoning |
|---|---|---|---|
| OLD 1 | Machine Learning KNN | 7 | K-Nearest Neighbor pattern recognition — classic ML |
| OLD 2 | Hurst Exponent | 7.5 | Trend vs mean-reversion regime detection — context setter |
| OLD 3 | Nadaraya-Watson Estimator | 7.5 | Kernel regression smoothing — dynamic support/resistance envelope |
| NEW 1 | ML Adaptive SuperTrend (2024) | 8 | K-Means clustering + volatility classification — adaptive trend |
| NEW 2 | DeepTrend AI (2023+) | 8 | LSTM/CNN hybrid, cross-asset pattern recognition — deep learning edge |
| ATR | ATR | 8 | AI signals ke saath bhi stop-loss discipline zaroori |
| S/R | Fibonacci Pivot | 7 | AI signal + Fib Pivot confluence = entry trigger |

**Combo Accuracy:** ~8.5/10 — Hurst Exponent (regime: trend ya range?) decide karta hai konsa indicator weight zyada dena hai. Trend regime mein ML Adaptive SuperTrend + DeepTrend AI lead karte hai; range mein Nadaraya-Watson envelope + KNN pattern lead karte hai. Fib Pivot dono regimes mein entry confirm karta hai.

**Logic:** Hurst Exponent > 0.5 (trending) → ML Adaptive SuperTrend + DeepTrend AI signal match + price Nadaraya-Watson envelope respect + Fibonacci Pivot confluence → Entry. (Hurst < 0.5 → range mode, KNN pattern + Nadaraya-Watson band touch + Fib Pivot priority). ATR stop.

---

## COMMON RULE (All 8 Desks)
Har desk apna result generate karega, lekin **final entry tabhi** jab:
- Index Green/Red (Desk ke direction se match)
- Sector Green/Red (Desk ke direction se match)
- Volume confirmation (above average)
- Candlestick pattern confirm
- Fibonacci Pivot S/R confluence (price entry-zone Fib level ke paas ho)

---

## SCANNER LAYOUT SUMMARY

| Desk # | Strategy Name | 3 Old | 2 New | Common |
|---|---|---|---|---|
| 1 | Indicator Based | ADX, RSI/Connors RSI, SuperTrend | ML Adaptive SuperTrend, RSI Velocity | ATR + Fib Pivot |
| 2 | Price Action | Anchored VWAP, Trendline, Candlestick | Order Block (SMC), Liquidity Sweep | ATR + Fib Pivot |
| 3 | Trend Following | Alpha Trend, Coral Trend, Schaff Trend Cycle | AutoTune Filter, Precision Trend Analysis | ATR + Fib Pivot |
| 4 | Momentum Reversal | WaveTrend, RSI, Fisher Transform | USI, Cybernetic Oscillator | ATR + Fib Pivot |
| 5 | Mean Reversion | Connors RSI, Laguerre RSI, Hull Suite | DVO, Enhanced Andean Oscillator | ATR + Fib Pivot |
| 6 | Smart Money | Order Block, FVG, Liquidity Sweeps | SMC (LuxAlgo), Volume Delta/CVD | ATR + Fib Pivot |
| 7 | Volume Breakout | Squeeze Momentum, Volume Profile, Cumulative Delta | SPOTVOL Index, Two-Pole Predictor | ATR + Fib Pivot |
| 8 | AI/ML Pattern | ML KNN, Hurst Exponent, Nadaraya-Watson | ML Adaptive SuperTrend, DeepTrend AI | ATR + Fib Pivot |

**Highest combo accuracy: Desk 6 (Smart Money) ~9/10** — institutional footprint sequence sabse complete hai.
