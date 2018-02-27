
PunycodeURL
===========

The original punycodeurl 0.1 for Python 2 remains unchanged, though moved to a separate file.  The equivalent functions for Python 3 are in a corresponding file and the module now detects calls the correct version depending on which version of Python is detected as in use.

punycodeurl
-----------

punycode encode for url

```python
import punycodeurl
punycodeurl.get('http://www.찰샴맨.com')
```

Installation
------------

To install for Python 2 run:

```shell
python setup.py install
```

To install for Python 3 run:

```shell
python3 setup.py install
```
