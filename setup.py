import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='punycodeurl',
      version='0.2',
      description='punycodeurl for Url',
      author='DaeMyung Kang',
      author_email='charsyam@gmail.com',
      url='https://github.com/charsyam/punycodeurl',
      platforms='any',
      install_requires=[],
          packages=['punycodeurl'],
          scripts=['punycodeurl/__init__.py', 'punycodeurl/punycodeurl2.py',
                   'punycodeurl/punycodeurl3.py'],
          classifiers=[
              'Intended Audience :: Developers',
              'License :: OSI Approved :: Apache LICENSE 2.0',
              'Topic :: Software Development :: Libraries :: Python Modules',
              'Topic :: Internet',
              'Programming Language :: Python :: 2',
              'Programming Language :: Python :: 2.7',
              'Programming Language :: Python :: 3',
              'Programming Language :: Python :: 3.4',
              'Programming Language :: Python :: 3.5',
              'Programming Language :: Python :: 3.6'
              ])
