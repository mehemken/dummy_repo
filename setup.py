########################################
#
# Author: Marco Hemken
# Email: mhemken@support.ucla.edu
#
# How to use this setup file
#
# $ python setup.py sdist
# $ pip install .
#
# The above commands will 1, create
# an installable module and 2, install
# the module. It is recommended you have
# a virtual environment active when
# you install this.

from distutils.core import setup

setup(
        name = 'dummylib',
        version = '0.1',
        py_modules = ['dummylib']
)
