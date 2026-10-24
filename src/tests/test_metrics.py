
import pytest

from llm_eval.metrics import (
    contains_required_facts,
    exact_match,
)


@pytest.mark.parametrize(
    ("actual", "expected"),
    [
        (
                "Customers can return items within 30 days.",
                "Customers can return items within 30 days.",
        ),
        (
                "  CUSTOMERS can return items within 30 days.  ",
                "Customers can return items within 30 days.",
        ),
    ],
)
def test_exact_match_passes_for_equivalent_text(
        actual: str,
        expected: str,
):
    assert exact_match(actual, expected)


def test_exact_match_fails_for_incorrect_answer():
    actual = "Customers can return items within 90 days."
    expected = "Customers can return items within 30 days."

    assert not exact_match(actual, expected)


def test_required_facts_pass_when_all_facts_are_present():
    answer = "Items can be returned within 30 days with a receipt."

    assert contains_required_facts(
        answer,
        ["30 days", "receipt"],
    )


def test_required_facts_fail_when_a_fact_is_missing():
    answer = "Items can be returned within 30 days."

    assert not contains_required_facts(
        answer,
        ["30 days", "receipt"],
    )
