.DEFAULT_GOAL := build
.PHONY: dependencies install test build clean

venv:
	@python -m venv venv

dependencies: venv
	@./venv/bin/pip install -r requirements.txt
	@./venv/bin/pip install -r requirements-test.txt

install: dependencies
	@./venv/bin/pip install -U pip
	@./venv/bin/pip install -e .[test]

build: test
	@./venv/bin/python -m build

test: install
	@./venv/bin/pytest test/

clean:
	@rm -rf dist battlemaster.egg-info