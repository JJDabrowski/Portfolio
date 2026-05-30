## Context

One of the main tasks of the project is that the code is readable and the project is well-organized

## Considered Options

* using autopep8 widget in VS Code
* adding pre-commit hooks containing black, flake8 and isort

## Decision Outcome

Chosen option: adding pre-commit hooks. Thanks to that on each commit when the files are changed, they will be automatically checked using black, flake8 and isort and thus they will conform to PEP8 and more