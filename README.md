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
response = jndlclient.search_text(title="test", cnt=1, from_date="2018-1-22")

print(response.to_json())
```

### argument (.search_text())

|Reference  |Contents                                        |Match criteria|multi  |
|:----------|:-----------------------------------------------|:-------------|:------|
|dpid       |Data Provider ID                                |Perfect match |able   |
|dpgroupid  |Data Provider Group ID                          |Perfect match |disable|
|any        |Search for all items                            |Partial Match |able   |
|title      |Title                                           |Partial Match |able   |
|creator    |Creator                                         |Partial Match |able   |
|publisher  |Publisher                                       |Partial Match |able   |
|ndc        |Classification(NDC)                             |Forward Match |disable|
|from_date  |Start Publication date(YYYY-MM-DD)              |              |disable|
|until_date |Finished publication date                       |              |disable|
|cnt        |Output record upper limit                       |              |disable|
|idx        |Record acquisition start position               |              |disable|
|isbn       |isbn                                            |              |disable|
|mediatype  |Type                                            |Perfect match |able   |

## Data Provider Group ID

|No |Data Provider Group ID    |Data Provider Group ID's Contents|
|:--|:-------------------------|:--------------------------------|
|1  |Digitalcontents           |                                 |
|2  |Catalogue                 |                                 |
|3  |Site                      |Site Information                 |
|4  |Reference                 |                                 |
|5  |Science                   |Natural Science                  |
|6  |Humanities                |                                 |
|7  |Library                   |                                 |
|8  |Child                     |                                 |
|9  |Ndl                       |                                 |

## Type

|symbol|Type|
|:-----|:---|
|1     |Book|
|2     |Articles/White Papper|
|3     |Newspaper|
|4     |Children's Book|
|5     |Reference Document|
|6     |Digital Document|
|7     |Other|
|8     |Document for handicapped people|
|9     |legislation Information|

Documentation
-------------

- [japnese README](./README.ja.md)


- Api document: http://iss.ndl.go.jp/information/api/
- NDC: http://www.libnet.pref.okayama.jp/shiryou/ndc/


Licence
-------------

[BSD-2-Clause](https://opensource.org/licenses/BSD-2-Clause)
