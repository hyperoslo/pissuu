#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name = 'pissuu',
    version = '0.0.1',
    description = 'Python client for the Issuu API',
    long_description = open('README.rst').read() + '\n\n' + open('HISTORY.rst').read(),
    author = 'Johannes Gorset',
    author_email = 'johannes@hyper.no',
    url = 'http://github.com/hyperoslo/pissuu',
    packages = [
        'pissuu'
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ],
    install_requires = [
        'requests >= 0.9, < 1.0'
    ]
)
