
PYTHON = python3
PYCOV = $(PYTHON) -m coverage
PYTEST = tests
SRC = ham

check:
	$(PYTHON) -m black --check --diff $(SRC)
	$(PYTHON) -m pylint -E            $(SRC)

format:
	$(PYTHON) -m black $(SRC)
	$(PYTHON) -m black $(PYTEST)


test:
	$(PYTHON) -m pytest $(PYTEST)

build:
	$(PYTHON) setup.py sdist

coverage:
	$(PYCOV) erase
	$(RM)  coverage.txt
	-$(PYCOV) run    -m "ham.cw.ntcexam"
	-$(PYCOV) run -a -m pytest
	$(PYCOV) report -m > ./coverage.txt

.DEFAULT_GOAL := fullcheck
fullcheck:
	$(MAKE) check
	$(MAKE) test
	$(MAKE) build
