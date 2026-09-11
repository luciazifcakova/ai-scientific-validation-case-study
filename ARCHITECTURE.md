# Validation Architecture

## Design principle

The generator and the validator should be treated as separate systems.

An AI-generated output should not become a downstream input merely because generation succeeded.

```text
generation != validation
```

A robust workflow introduces independent gates.

## Layer 1 — Structural validation

Questions:

- Is the output valid JSON / YAML / expected text format?
- Are required fields present?
- Are data types correct?
- Are identifiers syntactically valid?
- Are required sections non-empty?

Failure at this stage should stop the workflow immediately.

## Layer 2 — Dependency and API validation

For generated scientific code:

- are requested packages available?
- are functions / APIs valid?
- are versions compatible with the execution environment?
- is the requested dependency allowed?

This catches plausible-looking but nonexistent function names, obsolete APIs, and unsupported dependencies.

## Layer 3 — Security checks

Examples:

- filesystem access outside an allowed workspace;
- network access when it is not required;
- shell execution;
- destructive operations;
- dynamically generated commands that cannot be safely validated.

The objective is to reject unsafe output before execution.

## Layer 4 — Controlled execution

Only outputs passing the previous gates are executed.

Execution should capture:

- exit status;
- stdout / stderr;
- runtime;
- generated files;
- resource failures.

## Layer 5 — Output validation

Execution success does not imply scientific success.

Validate:

- required files exist;
- file formats are readable;
- required columns / fields exist;
- values fall within expected ranges;
- result objects are non-empty;
- downstream steps can consume the outputs.

## Layer 6 — Domain-specific validation

This is where generic software validation becomes scientific validation.

For bioinformatics / computational biology this may include:

- sequence constraints;
- taxonomic consistency;
- biological identifier verification;
- expected controls;
- data completeness;
- database cross-reference;
- biological plausibility checks.

## Layer 7 — Transparent decision

The output should conclude with an explicit decision:

```text
PASS
FAIL
REVIEW
```

and a machine-readable explanation of why.

This makes failures auditable and useful for improving both the AI generator and the surrounding workflow.
