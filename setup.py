from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
name='intakebuilder',
version='0.1dev',
packages=['intakebuilder',],
license='Creative Commons Attribution-Noncommercial-Share Alike license'
)
