from pprint import pprint
from setuptools import setup, find_packages
DOCNAME="Proj to Md"
PACKAGES = ['ham.' + p for p in find_packages('../ham')]

for p in PACKAGES:
    last = p.split('.')[-1]
    print(f"{DOCNAME} {last}\n===========================\n.. automodule:: {p}\n\t:members:\n\t:private-members:\n\t:special-members:\n\n")
