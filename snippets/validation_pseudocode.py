"""
Illustrative pseudocode only.

This file is not copied from a production system.
It demonstrates the control flow of a generic scientific-output
validation pipeline.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class ValidationResult:
    passed: bool
    stage: str
    messages: List[str]


def validate_schema(candidate) -> ValidationResult:
    # Example: check required fields, types, and structure.
    return ValidationResult(True, "schema", [])


def validate_dependencies(candidate) -> ValidationResult:
    # Example: verify requested packages/functions against an allowlist
    # or a known package/API registry.
    return ValidationResult(True, "dependencies", [])


def validate_security(candidate) -> ValidationResult:
    # Example: reject prohibited shell, filesystem, or network operations.
    return ValidationResult(True, "security", [])


def execute_in_controlled_environment(candidate) -> ValidationResult:
    # Example: run generated code in a sandbox/container and capture
    # exit status, stdout, stderr, and produced files.
    return ValidationResult(True, "execution", [])


def validate_outputs(candidate) -> ValidationResult:
    # Example: check that expected files/columns/results exist and
    # satisfy basic structural or scientific constraints.
    return ValidationResult(True, "outputs", [])


def validate(candidate):
    stages = [
        validate_schema,
        validate_dependencies,
        validate_security,
        execute_in_controlled_environment,
        validate_outputs,
    ]

    report = []

    for stage in stages:
        result = stage(candidate)
        report.append(result)

        # Fail fast: do not propagate an invalid output downstream.
        if not result.passed:
            return {
                "status": "REJECT",
                "failed_stage": result.stage,
                "report": report,
            }

    return {
        "status": "PASS",
        "report": report,
    }
