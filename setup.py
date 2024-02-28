from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
name='intakebuilder',
version='0.1.3',
packages=find_packages(),
include_package_data=True,
description='intake-esm Catalog Generation Utilities',
license='Creative Commons Attribution-Noncommercial-Share Alike license'
)


