SHELL := /bin/bash

.PHONY: help install lock update test test-unit test-integration test-system \
	tox lint format check docs clean

help:
	@echo "Useful tasks:"
	@echo "  make install           - install project and dependencies"
	@echo "  make lock              - regenerate poetry.lock"
	@echo "  make update            - update dependencies"
	@echo "  make test              - run all pytest tests"
	@echo "  make test-unit         - run unit tests"
	@echo "  make test-integration  - run integration tests"
	@echo "  make test-system       - run system tests"
	@echo "  make tox               - run tox default environments"
	@echo "  make lint              - run ruff + pylint"
	@echo "  make format            - run black + isort"
	@echo "  make check             - run poetry check"
	@echo "  make docs              - build docs"
	@echo "  make clean             - remove common cache/build artifacts"

install:
	poetry install

lock:
	poetry lock

update:
	poetry update

test:
	poetry run pytest -q

test-unit:
	poetry run pytest -m unit --cache-clear -q

test-integration:
	poetry run pytest -m integration --cache-clear -q

test-system:
	VIRTUAL_ENV="$$(poetry run python -c 'import sys; print(sys.prefix)')" poetry run pytest -m system --cache-clear -q

tox:
	poetry run tox

lint:
	pre-commit run --all-files

format:
	poetry run black src tests
	poetry run isort src tests

check:
	poetry check

docs:
	$$(MAKE) -C docs html

clean:
	rm -rf .pytest_cache .ruff_cache .mypy_cache .tox dist build .coverage* htmlcov
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
