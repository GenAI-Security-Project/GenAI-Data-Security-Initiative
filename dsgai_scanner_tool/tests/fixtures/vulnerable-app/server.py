"""Fixture MCP server — INTENTIONALLY VULNERABLE. Never deploy.

DSGAI06: uvicorn bound to 0.0.0.0 with no auth middleware (P06.5).
"""
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.post("/tool")
def run_tool(payload: dict):
    return {"ok": True}


if __name__ == "__main__":
    # DSGAI06 — bind-all with no auth (P06.5).
    uvicorn.run(app, host="0.0.0.0", port=8001)
