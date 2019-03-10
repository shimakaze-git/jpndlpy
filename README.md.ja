jpndlpy
====

jpndlpyは、国立国会図書館から図書情報を取得するためのrequestsのラッパーライブラリです。

## Description

jpndlpyは、日本国立国会図書館が出すopensearch(http://iss.ndl.go.jp/api/opensearch)APIから情報を取得し、json形式に整形します。

- Api document: http://iss.ndl.go.jp/information/api/
- NDC: http://www.libnet.pref.okayama.jp/shiryou/ndc/


## Install
jpndlpyのインストール方法

```bash
python setup.py install
```

```bash
pip3 install jpndlpy
```

## Usage
使用方法

``` python
jndlclient = JapanNdlClient()
# jndlclient.search_text(title="test", cnt=1, from_date="2018-1*22", until_date="tee")
# jndlclient.search_text(title="test", cnt=1, from_date="2018-1-22")
response = jndlclient.search_text(title="python", cnt=2)

print(response.to_json())
```

## Licence

[BSD-2-Clause](https://opensource.org/licenses/BSD-2-Clause)
