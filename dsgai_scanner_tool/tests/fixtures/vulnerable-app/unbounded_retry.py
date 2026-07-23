"""Intentionally vulnerable unbounded LLM retry loop."""


def ask_until_success(prompt):
    while True:
        response = chat(prompt)
        if response:
            return response
