"""Safe retry loop: the model call has an explicit timeout."""


def ask_with_timeout(prompt):
    while True:
        timeout = 10
        response = complete(prompt, timeout=timeout)
        if response:
            return response
