# Python Wrapper for Japan National Diet Library API(国立国会図書館 APIラッパーライブラリ)

Api document: http://iss.ndl.go.jp/information/api/
NDC: http://www.libnet.pref.okayama.jp/shiryou/ndc/

``` python

jndlclient = JapanNdlClient()
# jndlclient.search_text(title="test", cnt=1, from_date="2018-1*22", until_date="tee")
# jndlclient.search_text(title="test", cnt=1, from_date="2018-1-22")
response = jndlclient.search_text(title="python", cnt=2)

print(response.to_json())

```
