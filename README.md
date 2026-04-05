# Nightingale Intelligence

nightingale-core/
├── main.py                 # Entry point (FastAPI)
├── routers/                # Dedicated logic for each project
│   ├── vault.py            # Financial APIs (BTC, Macro, Trading)
│   ├── hh.py               # Planetary Data (Satellites, Air, Fire)
│   ├── living.py           # Natural Cycles (Lunar, Harvest)
│   └── wandering.py        # Aviation (OpenSky, Flight Data)
├── core/
│   ├── caching.py          # Redis/In-memory logic (saves API costs)
│   └── security.py         # API Key management & GDPR stripping
└── ai/
    ├── engine.py           # LLM logic (Gemini/GPT integration)
    └── context_pumps.py    # Merges API data into AI prompts
