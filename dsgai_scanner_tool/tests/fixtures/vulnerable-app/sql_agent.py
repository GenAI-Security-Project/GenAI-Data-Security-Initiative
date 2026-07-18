"""Fixture SQL agent — INTENTIONALLY VULNERABLE. Never deploy.

Genuine DSGAI12 violation: a LangChain SQL agent that executes LLM-generated
SQL directly. This is the true positive P12.1/P12.2 should catch (and that the
PR-11 rewrite must still catch, unlike webhook.py).
"""
from langchain_experimental.sql import SQLDatabaseChain
from langchain.agents import create_sql_agent


def build_agent(llm, db):
    # DSGAI12 FAIL signal — LangChain SQL agent (P12.2).
    agent = create_sql_agent(llm=llm, db=db, verbose=True)
    return agent


def run_generated(cursor, llm):
    # DSGAI12 FAIL — raw execution of LLM-generated SQL (P12.1).
    generated_sql = llm.generate("select all users")
    cursor.execute(generated_sql)
