import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.version_info[0] == 2:
    setup(name='punycodeurl',
          version='0.1',
          description='punycodeurl for Url',
          author='DaeMyung Kang',
          author_email='charsyam@gmail.com',
          url='https://github.com/charsyam/punycodeurl',
          platforms='any',
            install_requires=[],
            packages=['punycodeurl'],
            scripts=['punycodeurl/__init__.py']
            )
elif sys.version_info[0] == 3:
    setup(name='punycoder',
          version='0.2',
          description='punycoder for URL',
          author='Ben McGinnes',
          author_email='ben@adversary.org',
          url='https://github.com/Hasimir/punycodeurl',
          platforms='any',
          install_requires=[],
            packages=['punycoder'],
            scripts=['punycoder/__init__.py'],
            classifiers=[
                'Intended Audience :: Developers',
                'License :: OSI Approved :: Apache LICENSE 2.0',
                'Topic :: Software Development :: Libraries :: Python Modules',
                'Topic :: Internet',
                'Programming Language :: Python :: 3',
                'Programming Language :: Python :: 3.4',
                'Programming Language :: Python :: 3.5',
                'Programming Language :: Python :: 3.6'
                ])
                
