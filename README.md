# llm-quality-evaluation-framework


# LLM Quality Evaluation Framework

A Python-based framework for automated evaluation of AI-generated
answers, designed with a software quality engineering approach.

## Objectives

- Validate AI answers against expected results.
- Check whether responses contain required facts.
- Detect regressions using repeatable automated tests.
- Establish a foundation for LLM-as-a-judge and RAG evaluation.
- Integrate evaluation into CI/CD pipelines.

## Technology Stack

- Python 3.11+
- Pytest
- GitHub Actions (planned)
- DeepEval (planned)

## Current Features

- Text normalization
- Exact-match evaluation
- Required-fact validation
- Positive and negative automated tests
- Parameterized test scenarios

## Getting Started

Clone the repository and navigate to the project folder.

Create a virtual environment:

    python -m venv .venv

Activate it on Windows PowerShell:

    .\.venv\Scripts\Activate.ps1

Install the project and development dependencies:

    python -m pip install -e ".[dev]"

Run the evaluation tests:

    python -m pytest

## Planned Enhancements

1. Evaluation datasets in JSON format.
2. Answer relevance and faithfulness metrics.
3. Hallucination and prompt-injection test cases.
4. RAG evaluation.
5. JSON and HTML evaluation reports.
6. GitHub Actions CI/CD integration.

## Project Status

Initial implementation: deterministic answer evaluation.
LLM-based metrics and CI/CD are planned next.
