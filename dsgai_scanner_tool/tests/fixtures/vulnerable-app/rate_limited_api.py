"""Fixture GOOD inference endpoint — the negative case. Never deploy.

DSGAI20 PASS: the /chat endpoint requires auth and is rate limited
(P20.1 + P20.2), so the P20.5 "endpoint without auth/rate-limit" FAIL must
NOT fire here.
"""
from fastapi import Depends, FastAPI
from slowapi import Limiter

app = FastAPI()
limiter = Limiter(key_func=lambda: "global")


def require_auth():
    # DSGAI20 PASS — auth dependency (P20.1).
    return True


@app.post("/chat")
@limiter.limit("10/minute")
def chat(payload: dict, _auth: bool = Depends(require_auth)):
    # DSGAI20 PASS — rate limited (P20.2) and authenticated (P20.1).
    return {"reply": "ok"}
