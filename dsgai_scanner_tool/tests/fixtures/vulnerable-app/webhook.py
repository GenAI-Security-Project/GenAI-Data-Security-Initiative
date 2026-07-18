"""Fixture webhook handler — INTENTIONALLY part of the corpus.

This file contains NO LLM code. The db.execute below is an ordinary webhook
handler. v0.2 P12.1 wrongly flags it (the confirmed false positive, Appendix A
case 2). Expected: FAIL under v0.2 (known_bug), no finding after PR-11.
"""


def save_webhook(db, insert_stmt, response):
    # Normal webhook persistence. `response` is an HTTP response, not an LLM.
    db.execute(insert_stmt, response.json())
