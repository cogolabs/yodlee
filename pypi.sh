#!/usr/bin/env bash
# create a pypi acccount and .pypirc first
# https://packaging.python.org/distributing/#create-an-account
pip install -U twine wheel
python setup.py sdist bdist_wheel --universal
twine upload dist/* -r pypi
rm -fr build dist .egg yodlee.egg-info
