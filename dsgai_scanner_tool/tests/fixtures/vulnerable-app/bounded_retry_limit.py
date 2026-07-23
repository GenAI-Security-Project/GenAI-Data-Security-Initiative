"""Safe retry loop: a configured retry limit bounds attempts."""


def ask_with_retry_limit(prompt, max_retries):
    attempts = 0
    while True:
        if attempts >= max_retries:
            return None
        attempts += 1
        response = chat(prompt)
        if response:
            return response
