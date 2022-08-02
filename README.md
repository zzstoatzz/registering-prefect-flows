# Registering Prefect Flows using Docker Storage to ECR

## using `pre-commit` to guarantee a `requirements.txt`
we can populate our `pre-commit-config.yaml` with the hook that lives in `bin/update-requirements.sh` like:

```bash
repos:
- repo: https://github.com/zzstoatzz/registering-prefect-flows
  rev: 57a2089
  hooks:
  - id: update-requirements-from-pyproject

```
... which will create a `requirements.txt` file based on the `pyproject.toml` Poetry config file, if the `requirements.txt` is older than the `pyproject.toml` file.

This guarantees that an up-to-date `requirements.txt` will exist for CI/CD use during flow registration / image building.