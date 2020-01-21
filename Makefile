#!/usr/bin/make

pythonenv:
	virtualenv --python=python3 pythonenv
	pythonenv/bin/pip install -r requirements.txt

test: pythonenv
	@echo "### Running Python tests ###"
	pythonenv/bin/python -m nopea.tests.regression sqlite

package:
	pythonenv/bin/python setup.py sdist bdist_wheel

upload:
	pythonenv/bin/twine upload dist/* --verbose

lint:
	pythonenv/bin/flake8 . --count --ignore=F401,F403 --select=E9,F63,F7,F82 --show-source --statistics --exclude .git,__pycache__,pythonenv,migrations
	pythonenv/bin/flake8 . --count --ignore=F401,F403 --exit-zero --max-complexity=10 --max-line-length=127 --statistics --exclude .git,__pycache__,pythonenv,migrations

clean:
	rm -rf python*

PHONY: test clean pythonenv
