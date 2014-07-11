#!/usr/bin/env python
from setuptools import setup

NAME = 'introspect'
DESCRIPTION = 'how do you spend your time?'

VERSION = open('VERSION').read().strip()
LONG_DESC = open('README.rst').read()
LICENSE = open('LICENSE').read()
REQUIREMENTS = [open('requirements.txt').readlines()]

# TODO add classifiers
CLASSIFIERS = [
]

PACKAGES = ['introspect']
PACKAGE_DATA = {'introspect': ['scripts/osx_active_window_title.osascript']}

if __name__ == '__main__':
    setup(
        name=NAME,
        version=VERSION,
        author='Charles Thomas',
        author_email='ch@rlesthom.as',
        url='https://github.com/charlesthomas/%s' % NAME,
        license=LICENSE,
        description=DESCRIPTION,
        long_description=LONG_DESC,
        classifiers=CLASSIFIERS,
        install_requires=REQUIREMENTS,
        packages=PACKAGES,
        package_data=PACKAGE_DATA,
        test_suite='tests',
        entry_points='''
        [console_scripts]
        introspect_logger = introspect.introspect:logger
        ''',
    )
