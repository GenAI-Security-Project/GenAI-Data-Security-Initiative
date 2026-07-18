"""Fixture system prompt builder — INTENTIONALLY VULNERABLE. Never deploy.

DSGAI15 FAIL: a credential embedded directly in the system prompt string
(P15.1). Value-bearing — the scanner must locate but never echo the value.
"""

# DSGAI15 FAIL — secret embedded in system prompt (P15.1). Fake value.
system_prompt = "You are a helpful agent. Use api_key sk-proj-FAKE00000000000000000000000000 to call tools."
