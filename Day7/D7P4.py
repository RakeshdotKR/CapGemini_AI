"""Domain-specific prompt builders 
One canonical shape per domain (code, SQL, data analysis, business
writing) behind a registry, so callers never edit existing builders.
"""

from __future__ import annotations

from typing import Callable

# Registry: domain -> builder function
BUILDERS: dict[str, Callable[..., str]] = {}


def register(domain: str) -> Callable:
    """Decorator that adds a domain builder to the registry."""

    def decorator(func: Callable[..., str]) -> Callable[..., str]:
        BUILDERS[domain] = func
        return func

    return decorator


@register("code")
def code_prompt(language: str, task: str, edge_cases: list[str]) -> str:
    """Code generation: pin language, edge cases, and a no-prose contract."""
    edges = "\n".join(f"- {e}" for e in edge_cases)
    return (
        f"LANGUAGE: {language}\n"
        f"TASK: {task}\n"
        f"EDGE CASES TO HANDLE:\n{edges}\n"
        "RULES:\n"
        "- Output only code inside a single fenced block.\n"
        "- No explanations before or after the code.\n"
        "- Handle the edge cases explicitly."
    )


@register("sql")
def sql_prompt(dialect: str, schema: str, question: str) -> str:
    """SQL generation: pin dialect and schema; reads only, one statement."""
    return (
        f"DIALECT: {dialect}\n"
        "SCHEMA:\n"
        f"{schema}\n"
        f"QUESTION: {question}\n"
        "RULES:\n"
        "- SELECT statements only. No INSERT, UPDATE, DELETE, or DROP.\n"
        "- Exactly one statement; no semicolon-separated extras.\n"
        "- Alias every computed column."
    )


@register("data_analysis")
def analysis_prompt(dataset_note: str, question: str) -> str:
    """Data analysis: only supplied numbers, formula shown, 2-decimal rounding."""
    return (
        "You are a data analyst. Use ONLY the numbers below.\n"
        f"DATA:\n{dataset_note}\n"
        f"QUESTION: {question}\n"
        "RULES:\n"
        "- Show the arithmetic you performed.\n"
        "- Round every result to 2 decimal places.\n"
        "- Write 'not enough data' when a required number is missing."
    )


@register("business_writing")
def writing_prompt(audience: str, purpose: str, length: int) -> str:
    """Business writing: audience, purpose, length, plain language."""
    return (
        f"AUDIENCE: {audience}\n"
        f"PURPOSE: {purpose}\n"
        f"LENGTH: at most {length} words\n"
        "RULES:\n"
        "- Plain language; no jargon or acronyms without expansion.\n"
        "- One call to action at the end.\n"
        "- No hype words (game-changer, revolutionary)."
    )


def build_prompt(domain: str, **kwargs: object) -> str:
    """Render a prompt for a registered domain; raise on unknown domain."""
    if domain not in BUILDERS:
        raise ValueError(f"Unknown domain '{domain}'. "
                         f"Available: {', '.join(sorted(BUILDERS))}")
    builder = BUILDERS[domain]
    return builder(**kwargs)   # type: ignore[operator]


if __name__ == "__main__":
    print("=== code ===")
    print(build_prompt(
        "code",
        language="python",
        task="Parse a dotted version string into a tuple of ints",
        edge_cases=["non-numeric part raises ValueError",
                    "empty string raises ValueError"],
    ))

    print("\n=== sql ===")
    print(build_prompt(
        "sql",
        dialect="postgres",
        schema="orders(id, customer_id, total, created_at)",
        question="Revenue per customer for November 2026",
    ))

    print("\n=== data_analysis ===")
    print(build_prompt(
        "data_analysis",
        dataset_note="orders=1200, refunds=45, revenue_rs=840000",
        question="What is the refund rate and average order value?",
    ))

    print("\n=== business_writing ===")
    print(build_prompt(
        "business_writing",
        audience="all employees",
        purpose="Announce the new travel policy",
        length=120,
    ))

    try:
        build_prompt("legal_advice", question="Can I break my lease?")
    except ValueError as exc:
        print("\nError ->", exc)