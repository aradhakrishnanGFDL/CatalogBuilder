from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
name='intakebuilder',
packages=['intakebuilder',],
description='intake-esm Catalog Generation Utilities',
license='Creative Commons Attribution-Noncommercial-Share Alike license'
)
