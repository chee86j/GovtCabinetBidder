# Engineering Principles

## Core Rules

### KISS
Prefer the simplest implementation that solves the current problem.

### DRY
Do not duplicate business logic. Reuse existing logic when it keeps the code clearer.

### SRP
Each file and function should have one clear responsibility.

### YAGNI
Do not build features, abstractions, or configuration before they are needed.

### Code for humans first, computers second
Use readable names, simple control flow, and clear error messages.

### Fail fast
Validate inputs early and return useful errors as soon as a problem is known.

### Boy Scout Rule
Leave every touched file cleaner than you found it.

## How AI coding agents should work in this repo

- Make the smallest safe change.
- Run tests after each change.
- Do not rewrite unrelated files.
- Explain assumptions in comments or docs.
- Prefer typed interfaces and clear validation.
