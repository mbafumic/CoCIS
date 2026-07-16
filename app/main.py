from fastapi import FastAPI

from app.api.routers import pazienti, prenotazioni, prericoveri, ricoveri

app = FastAPI(title="CoCIS API")

app.include_router(pazienti.router)
app.include_router(prenotazioni.router)
app.include_router(prericoveri.router)
app.include_router(ricoveri.router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
