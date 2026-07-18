"""Fixture telemetry init — INTENTIONALLY VULNERABLE. Never deploy.

DSGAI14 WARN: Langfuse initialised with full content capture enabled (P14.2),
which logs full prompt/response content.
"""
from langfuse import Langfuse


def init_tracing():
    # DSGAI14 WARN — prompt/response content capture enabled (P14.2).
    return Langfuse(capture_content=True)
