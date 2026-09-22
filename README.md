# Reusable Workflow Python

A sample Python Flask application that demonstrates how to **call and use a GitHub Actions reusable workflow** stored in another repository.

## Overview

This repository contains a small Flask API and a GitHub Actions caller workflow.

Project structure:

```text
reusable-caller-workflow-python/
├── app/
│   └── __init__.py
├── requirements.txt
├── tests/
│   └── test_app.py
├── .github/
│   └── workflows/
│       └── ci.yml
└── README.md
```

## Application

The application provides two endpoints:

### Health Check

```text
GET /health
```

Example response:

```json
{
  "status": "healthy",
  "service": "reusable-workflow-python-api"
}
```

### Users

```text
GET /api/users
```

The endpoint returns a small sample list of users.

## Dependencies

The project uses:

```text
Flask==3.1.2
pytest==8.4.2
```

## Local Setup

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Linux/macOS:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m app
```

Run tests:

```bash
PYTHONPATH=. pytest
```

## GitHub Actions Caller Workflow

The GitHub Actions workflow is stored at:

```text
.github/workflows/ci.yml
```

Current workflow:

```yaml
name: Python Application CI

on:
  push:
    branches:
      - main

jobs:
  call-common-ci:
    uses: Satyajeet-Sah/reusable-workflow/.github/workflows/common-ci.yml@main
    with:
      python-version: "3.12"
```

## How the Reusable Workflow Works

When code is pushed to the `main` branch:

```text
Push to main
     │
     ▼
ci.yml starts
     │
     ▼
calls common-ci.yml
     │
     ▼
reusable-workflow
     │
     ├── Checkout caller repository
     ├── Setup Python 3.12
     ├── Install dependencies
     ├── Check project files
     └── Run pytest
```

The reusable workflow is stored in a separate repository:

```text
Satyajeet-Sah/reusable-workflow
```

and is called with:

```yaml
uses: Satyajeet-Sah/reusable-workflow/.github/workflows/common-ci.yml@main
```

## Passing an Input

The reusable workflow accepts a `python-version` input.

The caller passes:

```yaml
with:
  python-version: "3.12"
```

The reusable workflow receives it through:

```yaml
on:
  workflow_call:
    inputs:
      python-version:
        type: string
        default: "3.12"
```

and uses it with:

```yaml
python-version: ${{ inputs.python-version }}
```

This allows different caller repositories to select the Python version without changing the common workflow.

For example:

```yaml
with:
  python-version: "3.11"
```

or:

```yaml
with:
  python-version: "3.13"
```

## Why Use a Reusable Workflow?

Without a reusable workflow, every Python repository may need to maintain its own CI steps.

With a reusable workflow:

```text
Python App 1 ──┐
Python App 2 ──┤
Python App 3 ──┼──> Common CI workflow
Python App 4 ──┤
Python App 5 ──┘
```

The common CI logic is maintained in one repository and reused by multiple projects.

## Key Concepts Learned

- `ci.yml` is the **caller workflow**.
- `common-ci.yml` is the **reusable workflow**.
- `workflow_call` allows another workflow to call `common-ci.yml`.
- `uses:` references the reusable workflow.
- `with:` passes input values.
- `inputs.python-version` receives the passed value.
- The reusable workflow can operate on the caller repository's code.
- A push to `main` in this repository triggers the caller workflow.

## Repository Relationship

```text
reusable-caller-workflow-python
              │
              │ ci.yml
              │
              │ uses
              ▼
       reusable-workflow
              │
              │ common-ci.yml
              ▼
           python-ci
```

## Reusable Workflow Repository

This project uses the reusable workflow from the repository below:

[reusable-workflow](https://github.com/Satyajeet-Sah/reusable-workflow)
