# 🦅 GARUDA POWER — Trading Scanner System

## Architecture
```
Angel One API
      ↓
backend/angel_api.py     ← Data fetch (Python)
      ↓
backend/scanners/*.py    ← 11 Scanners (Pandas)
      ↓
backend/server.js        ← WebSocket Server (Node.js)
      ↓
frontend/garuda-power-*.html  ← UI Pages (A-K)
      ↓
frontend/master-panel.html    ← Master Control Panel
```

## Folder Structure
```
garuda-power/
├── backend/
│   ├── server.js           ← Node.js WebSocket server
│   ├── angel_api.py        ← Angel One API connector
│   ├── run_scanners.py     ← Runs all 11 scanners
│   ├── requirements.txt    ← Python dependencies
│   ├── package.json        ← Node.js dependencies
│   └── scanners/
│       ├── scanner_a.py    ← Pattern Scanner
│       ├── scanner_b.py    ← Oscillator Scanner
│       ├── scanner_c.py    ← Advanced Fusion
│       ├── scanner_d.py    ← Command Scanner
│       ├── scanner_e.py    ← Scanner E
│       ├── scanner_f.py    ← Scanner F
│       ├── scanner_g.py    ← Scanner G
│       ├── scanner_h.py    ← Scanner H
│       ├── scanner_i.py    ← Scanner I
│       ├── scanner_j.py    ← Scanner J
│       └── scanner_k.py    ← Scanner K
├── frontend/
│   ├── garuda-power-a.html
│   ├── ... (B to K)
│   └── master-panel.html
├── scripts/
│   └── deploy.sh           ← Digital Ocean deploy script
└── README.md
```

## Quick Deploy on Digital Ocean
```bash
git clone https://github.com/charanpuransinh/garuda-power
cd garuda-power
bash scripts/deploy.sh
```
