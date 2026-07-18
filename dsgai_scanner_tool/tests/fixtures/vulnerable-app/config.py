"""Fixture config — INTENTIONALLY VULNERABLE. Fake values only. Never deploy.

Quoted hardcoded key: the case v0.2 P02.1 already catches (quote required).
"""

# DSGAI02 FAIL — hardcoded OpenAI key, quoted (P02.1 matches under v0.2).
OPENAI_API_KEY = "sk-proj-FAKE00000000000000000000000000"

MODEL = "gpt-4o-mini"
TEMPERATURE = 0.2
