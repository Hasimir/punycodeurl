#!/usr/bin/env python3

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='punycoder',
        version='0.2',
        description='punycoder for URL',
        author='Ben McGinnes',
        author_email='ben@adversary.org',
        url='https://github.com/Hasimir/punycodeurl',
        platforms='any',
        install_requires=[],
        packages=['punycoder'],
        classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache LICENSE 2.0',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Internet',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
        scripts=['punycoder/__init__.py']
        )
