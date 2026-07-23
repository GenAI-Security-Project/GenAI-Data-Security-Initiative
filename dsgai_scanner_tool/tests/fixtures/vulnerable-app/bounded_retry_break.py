"""Safe retry loop: an explicit break condition bounds the loop."""


def ask_while_available(prompt, should_stop):
    while True:
        if should_stop():
            break
        generate(prompt)
