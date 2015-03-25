from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from setuptools import setup, find_packages

version = '0.1.13'

setup(
    name='ripozo-tests',
    version=version,
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    description='A helper package for creating tests for ripozo and its extensions',
    author='Tim Martin',
    author_email='tim.martin@vertical-knowledge.com',
    install_requires=['six>=1.4.1,!=1.7.1'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4'
    ]
)
