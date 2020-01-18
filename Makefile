#!/usr/bin/make

pythonenv:
	python3 -m venv pythonenv
	pythonenv/bin/pip install mysqlclient==1.3.10 colorama==0.3.9 ipython==6.4.0

test: pythonenv
	@echo "### Running Python tests ###"
	pythonenv/bin/python -m nopea.tests

package:
	pythonenv/bin/python setup.py sdist bdist_wheel

upload:
	pythonenv/bin/twine upload dist/*

clean:
	rm -rf python*

PHONY: test clean
