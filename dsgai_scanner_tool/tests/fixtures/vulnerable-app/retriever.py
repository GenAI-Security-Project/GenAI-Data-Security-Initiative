"""Fixture RAG retriever — INTENTIONALLY VULNERABLE. Never deploy.

DSGAI11: the first vector query has no tenant filter (P11.1 FAIL — no P11.2
within +/-15 lines). The second query, kept well beyond the proximity window
on purpose, carries a tenant filter (P11.2 PASS signal).
"""


def search_no_tenant(vectorstore, query):
    # DSGAI11 FAIL — no tenant isolation on the query.
    # P11.1 fires here; there is no tenant filter within 15 lines below.
    return vectorstore.similarity_search(query, k=5)


# ---------------------------------------------------------------------------
# The tenant-scoped variant lives here, deliberately more than 15 lines away
# from the unscoped query above so the proximity check treats them as two
# independent call sites and does not let the filter below "rescue" the query
# above. Padding kept intentionally verbose for exactly this reason.
# ---------------------------------------------------------------------------


def _audit_note():
    # Filler to keep the two call sites outside each other's proximity window.
    return "unscoped and scoped retrieval are evaluated independently"


def search_scoped(vectorstore, query, tid):
    # DSGAI11 PASS — tenant filter present.
    return vectorstore.similarity_search(query, k=5, filter={"tenant_id": tid})
