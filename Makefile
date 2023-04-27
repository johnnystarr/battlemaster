.DEFAULT_GOAL := build
.PHONY: dependencies install test build clean
VENV_BIN = ./venv/bin
PIP = $(VENV_BIN)/pip
PYTHON = $(VENV_BIN)/python
PYTEST = $(VENV_BIN)/pytest
PYLINT = $(VENV_BIN)/pylint

venv:
	@python -m venv venv

dependencies: venv
	@$(PIP) install -r requirements.txt
	@$(PIP) install -r requirements-test.txt

install: dependencies
	@$(PIP) install -U pip
	@$(PIP) install -e .[test]

build: test
	@$(PYTHON) -m build

lint:
	@$(PYLINT) battlemaster/

test: install lint
	@$(PYTEST) test/

clean:
	@rm -rf dist battlemaster.egg-info