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
response = jndlclient.search_text(title="test", cnt=1, from_date="2018-1-22")

print(response.to_json())
```

### argument (.search_text())

|参照名     |内容                                            |一致条件|複数   |
|:----------|:-----------------------------------------------|:-------|:------|
|dpid       |データプロパイダID                              |完全一致|able   |
|dpgroupid  |データプロバイダグループID                      |完全一致|disable|
|any        |すべての項目を対象に検索                        |部分一致|able   |
|title      |タイトル                                        |部分一致|able   |
|creator    |作成者                                          |部分一致|able   |
|publisher  |出版者                                          |部分一致|able   |
|ndc        |分類(NDC)                                       |前方一致|disable|
|from_date  |開始出版年月日(YYYY-MM-DD)                      |        |disable|
|until_date |終了出版年月日                                  |        |disable|
|cnt        |出力レコード上限値(省略時は200)                 |        |disable|
|idx        |レコード取得開始位置                            |        |disable|
|isbn       |isbn(10, 13桁の場合は完全一致), その他は前方一致|        |disable|
|mediatype  |種類種別                                        |完全一致|able   |

## データプロバイダグループID

|No |データプロバイダグループID|データプロバイダグループIDの内容|
|:--|:-------------------------|:-------------------------------|
|1  |Digitalcontents           |本文、デジタル画像等(一次情報)  |
|2  |Catalogue                 |目録、索引等                    |
|3  |Site                      |サイト情報                      |
|4  |Reference                 |調べ物に便利な情報、参考情報    |
|5  |Science                   |自然科学系の情報                |
|6  |Humanities                |人文科学系の情報                |
|7  |Library                   |図書館に関わる情報              |
|8  |Child                     |子供向けの情報                  |
|9  |Ndl                       |国立国会図書館が提供する情報    |

## 種類種別

|記号|種別|
|:---|:---|
|1   |本  |
|2   |記事・論文|
|3   |新聞|
|4   |児童書|
|5   |レファレンス資料|
|6   |デジタル資料|
|7   |その他|
|8   |障害者向け資料|
|9   |立法情報|

Documentation
-------------

- [japnese README](./README.ja.md)


- Api document: http://iss.ndl.go.jp/information/api/
- NDC: http://www.libnet.pref.okayama.jp/shiryou/ndc/


Licence
-------------

[BSD-2-Clause](https://opensource.org/licenses/BSD-2-Clause)
