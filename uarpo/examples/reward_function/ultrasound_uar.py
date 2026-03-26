# Copyright 2024 Bytedance Ltd. and/or its affiliates
#
# Ultrasound Answer Reward (UAR) — implements:
#   R(x, y) = R_format(y) + λ * R_gate(y) * R_outcome(x, y)
#
# R_gate ∈ {0, 1} gates clinical outcome reward until format/reporting constraints are met.
# Tune section headers, regex, and `lambda_outcome` to match your reporting rubric.

import re
from typing import Dict


def _format_reward(text: str) -> float:
    """Structural / template compliance (placeholder: section tags present)."""
    required = ("FINDINGS", "IMPRESSION")
    upper = text.upper()
    hits = sum(1 for k in required if k in upper)
    return float(hits) / len(required)


def _gate_reward(text: str) -> float:
    """1 iff predefined reporting constraints satisfied; else 0."""
    # Example: both FINDINGS and IMPRESSION blocks with non-empty body.
    pat = re.compile(
        r"FINDINGS\s*:\s*(.+?)(?=IMPRESSION|\Z)",
        re.IGNORECASE | re.DOTALL,
    )
    pat_imp = re.compile(
        r"IMPRESSION\s*:\s*(.+?)\Z",
        re.IGNORECASE | re.DOTALL,
    )
    m1, m2 = pat.search(text), pat_imp.search(text)
    if not m1 or not m2:
        return 0.0
    body1, body2 = m1.group(1).strip(), m2.group(1).strip()
    return 1.0 if len(body1) >= 8 and len(body2) >= 4 else 0.0


def _outcome_reward(predict: str, ground_truth: str) -> float:
    """Task-level clinical correctness (placeholder: label match in IMPRESSION)."""
    pat = re.compile(r"IMPRESSION\s*:\s*(.+?)(?:\n|$)", re.IGNORECASE | re.DOTALL)
    m = pat.search(predict)
    impression = m.group(1).strip().lower() if m else predict.strip().lower()
    gt = (ground_truth or "").strip().lower()
    if not gt:
        return 0.0
    return 1.0 if gt in impression or impression in gt else 0.0


def compute_score(
    predict: str,
    ground_truth: str,
    lambda_outcome: float = 1.0,
) -> Dict[str, float]:
    r_fmt = _format_reward(predict)
    r_gate = _gate_reward(predict)
    r_out = _outcome_reward(predict, ground_truth)
    overall = r_fmt + float(lambda_outcome) * r_gate * r_out
    return {
        "overall": overall,
        "format": r_fmt,
        "gate": r_gate,
        "outcome": r_out,
        "accuracy": r_out,
    }
