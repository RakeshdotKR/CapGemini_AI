"""Prompt evaluation runner 
Runs a fixed eval set against a predictor and reports per-metric
pass rates - the smallest useful eval loop.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable

@dataclass(frozen=True)
class EvalCase:
    case_id: str
    user_input: str
    expected: str
    tags: tuple[str, ...] = ()

def exact_match(prediction:str, expected: str)->bool:
    return prediction.strip().lower() == expected.strip().lower()

def contains_terms(prediction:str, expected: str)->bool:
    lowered = prediction.lower()
    return all(term in lowered for term in expected.lower().split())

METRICS: dict[str,Callable[[str,str],bool]] = {
    "exact_match":exact_match,
    "contains_terms": contains_terms,
}

@dataclass
class EvalReport:
    total: int = 0
    passed: int = 0
    failures: list[str] = field(default_factory=list)

    @property
    def pass_rate(self) -> float:
        return self.passed / self.total if self.total else 0.0


def run_eval(
    cases: list[EvalCase],
    predict: Callable[[str], str],
    metric_name: str = "exact_match",
) -> EvalReport:
    """Run every case through `predict` and score with a named metric."""
    if metric_name not in METRICS:
        raise ValueError(f"Unknown metric '{metric_name}'. "
                         f"Available: {', '.join(sorted(METRICS))}")
    metric = METRICS[metric_name]
    report = EvalReport()
    for case in cases:
        prediction = predict(case.user_input)
        report.total += 1
        if metric(prediction, case.expected):
            report.passed += 1
        else:
            report.failures.append(
                f"{case.case_id}: expected {case.expected!r}, "
                f"got {prediction!r}"
            )
    return report


if __name__ == "__main__":
    # Stand-in model: canned answers keyed by input (a real eval calls the API)
    CANNED = {
        "Where is my order 5566?": "Order 5566 shipped on 12 Nov.",
        "What is the return window?": "Returns are allowed within 30 days.",
        "Is order 9999 delivered?": "I do not know.",          # weak answer
        "Who are you?": "I am a shopping assistant.",
    }

    def predict(user_input: str) -> str:
        return CANNED.get(user_input, "")

    cases = [
        EvalCase("c1", "Where is my order 5566?", "5566 shipped"),
        EvalCase("c2", "What is the return window?", "30 days"),
        EvalCase("c3", "Is order 9999 delivered?", "delivered"),
        EvalCase("c4", "Who are you?", "shopping assistant"),
    ]

    for metric in ("exact_match", "contains_terms"):
        report = run_eval(cases, predict, metric_name=metric)
        print(f"{metric:15}: pass_rate={report.pass_rate:.0%} "
              f"({report.passed}/{report.total})")
        for failure in report.failures:
            print("   fail:", failure)

    try:
        run_eval(cases, predict, metric_name="bleu")
    except ValueError as exc:
        print("Error ->", exc)
