
PYTHON = python3
PYTEST = test
SRC = ham

check:
	$(PYTHON) -m black --check --diff $(SRC)
	$(PYTHON) -m pylint -E            $(SRC)

format:
	$(PYTHON) -m black $(SRC)

test:
	$(PYTHON) -m pytest $(PYTEST)

build:
	$(PYTHON) setup.py sdist

.DEFAULT_GOAL := fullcheck
	$(MAKE) check
	$(MAKE) test
	$(MAKE) build