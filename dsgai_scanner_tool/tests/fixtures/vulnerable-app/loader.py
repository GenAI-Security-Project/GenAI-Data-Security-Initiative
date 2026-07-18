"""Fixture model loader — INTENTIONALLY VULNERABLE. Never deploy.

DSGAI04 FAIL: torch.load without weights_only=True (P04.1 minus P04.2).
"""
import torch


def load_model(model_path):
    # DSGAI04 FAIL — unsafe pickle deserialization (no weights_only=True).
    model = torch.load(model_path)
    return model
