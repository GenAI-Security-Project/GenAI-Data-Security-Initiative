"""Fixture JWT literal — INTENTIONALLY VULNERABLE. Fake values only. Never deploy.

DSGAI02 WARN (P02.10): a JWT hardcoded in source. JWT-shaped strings are often
public test tokens, so the rule is low confidence and a hit is a WARN, not a FAIL.
The token is unsigned ({"alg":"none"}) with a fake payload and signature.
"""
SERVICE_JWT = "eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJzdWIiOiJGQUtFIn0.FAKE0000000000000000000000"
