
"""Basic metrics for evaluating AI-generated answers."""


def normalize(text: str) -> str:
    """Normalize text for simple comparisons."""
    return " ".join(text.casefold().split())


def exact_match(actual: str, expected: str) -> bool:
    """Check whether two answers match after normalization."""
    return normalize(actual) == normalize(expected)


def contains_required_facts(
        actual: str,
        required_facts: list[str],
) -> bool:
    """Check whether all required facts appear in an answer."""
    normalized_answer = normalize(actual)

    return all(
        normalize(fact) in normalized_answer
        for fact in required_facts
    )
