
VENV_NAME?=pe38
VENV_ACTIVATE=. ~/$(VENV_NAME)/bin/activate
PYTHON=~/${VENV_NAME}/bin/python3
PIP = pip3
PYCOV = $(PYTHON) -m coverage
PYTEST = tests
SRC = ham
Package = NTCC-0.0a.tar.gz

.DEFAULT_GOAL := fullcheck
fullcheck:
	$(MAKE) check
	$(MAKE) test
	$(MAKE) build
	$(MAKE) install


.PHONY: build
build:
	$(PYTHON) setup.py sdist

check:
	$(PYTHON) -m black --check --diff $(SRC)
	$(PYTHON) -m pylint -E            $(SRC)

coverage:
	$(PYCOV) erase
	$(RM)  coverage.txt
	-$(PYCOV) run    -m "ham.cw.ntcexam"
	-$(PYCOV) run -a -m pytest
	$(PYCOV) report --source=$(SRC) -m > ./coverage.txt

.PHONY: doc
doc:
	$(VENV_ACTIVATE) && cd Doc; make html

dist:
	$(PYTHON) setup.py sdist

format:
	$(PYTHON) -m black $(SRC)
	$(PYTHON) -m black $(PYTEST)

.PHONY: install
install:
	${PYTHON} -m pip install -e .

test:
	$(PYTHON) -m pytest $(PYTEST)

<<<<<<< HEAD
.PHONY: build
build:
	$(PYTHON) setup.py sdist
	-$(PIP) install "./dist/$(Package)"

paris:
	$(PYTHON) -m "ham.cw.paris"

coverage:
	$(PYCOV) erase
	$(RM)  coverage.txt
	-$(PYCOV) run    -m "ham.cw.ntcexam"
	-$(PYCOV) run -a -m pytest
	$(PYCOV) report --source=$(SRC) -m > ./coverage.txt

.PHONY: doc
doc:
	$(VENV_ACTIVATE) && cd Doc; make html

.DEFAULT_GOAL := fullcheck
fullcheck:
	$(MAKE) check
	$(MAKE) test
	$(MAKE) build
=======
#
# These are specific to this project
#
exam:
	$(PYTHON) -m "ham.cw.ntcexam"

paris:
	$(PYTHON) -m "ham.cw.paris"
