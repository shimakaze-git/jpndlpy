import os
import sys
import unittest

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)


from jpndlpy import JapanNdlClient


class JpndlpyTest(unittest.TestCase):

    def test_jpndlpy_cnt_50_over(self):
        title = "python"
        cnt = 50

        jpdlclient = JapanNdlClient()
        response = jpdlclient.search_text(title=title, cnt=cnt)

        self.assertEqual(jpdlclient.search_title, title)
        self.assertEqual(type(response.to_json()), dict)

    # def test_jpndlpy_cnt_300_over(self):
    #     title = "python"
    #     cnt = 300

    #     jpdlclient = JapanNdlClient()
    #     response = jpdlclient.search_text(title=title, cnt=cnt)
    #     print(jpdlclient.search_title)


if __name__ == "__main__":
    unittest.main()
