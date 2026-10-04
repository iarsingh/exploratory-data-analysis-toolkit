from fastapi import FastAPI, HTTPException
from eda.analyze import InputError, analyze

app = FastAPI()


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.post("/analyze")
def post_analyze(body: dict):
    try:
        return analyze(body.get("rows"))
    except InputError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
