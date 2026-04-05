from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import vault, hh, living, wandering

app = FastAPI(title="Nightingale Intelligence Core")

# Allow your subdomains to talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://vault.nightingaleint.com", "https://hh.nightingaleint.com"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connect your projects
app.include_router(vault.router, prefix="/v1/vault")
app.include_router(hh.router, prefix="/v1/hh")
app.include_router(living.router, prefix="/v1/living")
app.include_router(auth.router, prefix="/v1/auth", tags=["Auth"])

@app.get("/")
async def root():
    return {"status": "Nightingale Intelligence Core Online"}
