import os
import sys
import unittest

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)


# from jpndlpy.client import JapanNdlClient
from jpndlpy import JapanNdlClient


class JondlpyTest(unittest.TestCase):

    def test_jpndlpy(self):
        title = "python"
        cnt = 2

        jndlclient = JapanNdlClient()
        # jndlclient.search_text(title="test", cnt=1, from_date="2018-1*22", until_date="tee")
        # jndlclient.search_text(title="test", cnt=1, from_date="2018-1-22")
        response = jndlclient.search_text(title=title, cnt=cnt)
        print(response.to_json())

        self.assertEqual(jndlclient.search_title, title)
        self.assertEqual(type(response.to_json()), dict)

if __name__ == "__main__":
    unittest.main()
