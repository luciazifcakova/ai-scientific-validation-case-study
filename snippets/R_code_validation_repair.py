#validator logic for llm generated output:
api_validator = RApiValidator(
    teaching_packages=primary_packages,
    allowed_packages=allowed_packages,
    api_report=package_api,
)

validation = RCodeValidator(
    allowed_packages=allowed_packages,
    enforce_package_allowlist=True,
).validate(
    validated.code,
    expected_outputs,
)

validation_errors = [
    f"{issue.rule}: {issue.message}"
    for issue in validation.issues
    if issue.severity == "error"
]

api_issues = api_validator.validate(validated.code)
validation_errors.extend(
    api_validator.feedback(api_issues)
)

if validation_errors:
 raise ValueError("; ".join(validation_errors))


#repair logic is:
except Exception as exc:
    final_errors = self._validation_messages(exc)

    attempts.append(
        RCodeGenerationAttempt(
            task_id=task.task_id,
            attempt=attempt_number,
            succeeded=False,
            validation_errors=final_errors,
            ...
        )
    )

    if attempt_number < self.max_attempts:
        user_prompt = self._repair_user_prompt(
            original_user=original_user,
            previous_response=raw_response,
            errors=final_errors,
        )
