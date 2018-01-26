#!/usr/bin/env python

import os

from setuptools import setup

module_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    setup(
        name='ctrn',
        version='0.0.1',
        description='',
        long_description=open(os.path.join(module_dir, 'README.md')).read(),
        url='https://github.com/matk86/ctrn',
        author='Kiran Mathew',
        author_email='kmathew@lbl.gov',
        zip_safe=False,
        install_requires=['pymongo>=3.6.0'],
        classifiers=["Programming Language :: Python :: 3",
                     "Programming Language :: Python :: 3.6",
                     'Operating System :: OS Independent',
                     'Topic :: Other/Nonlisted Topic'],
        test_suite='nose.collector',
        tests_require=['nose']
)
