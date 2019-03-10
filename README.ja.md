Jpndlpy: HTTP Client for the Japan National Diet Library API.
========
[![image](https://img.shields.io/pypi/v/jpndlpy.svg)](https://pypi.org/project/jpndlpy/)
[![image](https://img.shields.io/pypi/l/jpndlpy.svg)](https://pypi.org/project/jpndlpy/)
[![image](https://img.shields.io/pypi/pyversions/jpndlpy.svg)](https://pypi.org/project/jpndlpy/)

**jpndlpyは、国立国会図書館APIから図書情報を取得するためのrequestsのラッパーライブラリです。**


Description
------------

jpndlpyは、日本国立国会図書館が出すopensearch(http://iss.ndl.go.jp/api/opensearch) APIから情報を取得し、json形式に整形します。

Installation
------------

jpndlpyのインストール方法

``` {.sourceCode .bash}
$ python setup.py install
```

```bash
$ pip3 install jpndlpy
```

Usage
------------

使用方法とサンプルコード

``` python
jndlclient = JapanNdlClient()
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
