from fastapi import FastAPI

from . import api_incidents

app = FastAPI(title="Suraksha Desk API", version="0.1.0")

app.include_router(api_incidents.router)


@app.get("/health")
def health():
    return {"status": "ok", "service": "suraksha-desk-api"}
