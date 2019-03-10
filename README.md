Jpndlpy: HTTP Client for the Japan National Diet Library API.
========
[![image](https://img.shields.io/pypi/v/jpndlpy.svg)](https://pypi.org/project/jpndlpy/)
[![image](https://img.shields.io/pypi/l/jpndlpy.svg)](https://pypi.org/project/jpndlpy/)
[![image](https://img.shields.io/pypi/pyversions/jpndlpy.svg)](https://pypi.org/project/jpndlpy/)

**jpndlpy is a requests wrapper library for obtaining book information from the Japan National Diet Library.**


## Description

jpndlpy is gets information from opensearch provided by the Japan National Diet Library, and The obtained data is converted to json format.

Installation
------------

How to install jpndlpy

``` {.sourceCode .bash}
$ python setup.py install
```

```bash
$ pip3 install jpndlpy
```

Usage
------------

How to Use

sample code

``` python
jndlclient = JapanNdlClient()
# jndlclient.search_text(title="test", cnt=1, from_date="2018-1*22", until_date="tee")
# jndlclient.search_text(title="test", cnt=1, from_date="2018-1-22")
response = jndlclient.search_text(title="python", cnt=2)

print(response.to_json())
```

Documentation
-------------

- [japnese README](./README.ja.md)


- Api document: http://iss.ndl.go.jp/information/api/
- NDC: http://www.libnet.pref.okayama.jp/shiryou/ndc/


Licence
-------------

[BSD-2-Clause](https://opensource.org/licenses/BSD-2-Clause)
