#!/usr/bin/make

pythonenv:
	virtualenv --python=python3 pythonenv
	pythonenv/bin/pip install -r requirements.txt

test: pythonenv
	@echo "### Running Python tests ###"
	pythonenv/bin/python -m nopea.tests

package:
	pythonenv/bin/python setup.py sdist bdist_wheel

upload:
	pythonenv/bin/twine upload dist/*

clean:
	rm -rf python*

PHONY: test clean pythonenv
