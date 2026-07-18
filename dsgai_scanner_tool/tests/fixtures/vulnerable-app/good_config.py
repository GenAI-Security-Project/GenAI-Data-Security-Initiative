"""Fixture GOOD config — the negative case. Never deploy (it's still a fixture).

DSGAI02 PASS signal: the API key is retrieved from Vault at runtime via a
Vault client (P02.7), not hardcoded. No FAIL rule should fire here.
"""
import hvac


def get_openai_key():
    # DSGAI02 PASS — secret pulled from Vault, never hardcoded (P02.7).
    client = hvac.Client(url="https://vault.internal:8200")
    secret = client.secrets.kv.v2.read_secret_version(path="openai")
    return secret["data"]["data"]["api_key"]
