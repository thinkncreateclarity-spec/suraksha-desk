from fastapi import FastAPI

app = FastAPI(title="Suraksha Desk API", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok", "service": "suraksha-desk-api"}
