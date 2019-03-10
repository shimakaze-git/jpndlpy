import os
import sys
import unittest

import pprint

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

# from jpndlpy.client import JapanNdlClient
from jpndlpy import JapanNdlClient


class JondlpyClientTest(unittest.TestCase):

    def test_search_text(self):
        title = "python"
        cnt = 2

        jndlclient = JapanNdlClient()
        response = jndlclient.search_text(title=title, cnt=cnt)
        pprint.pprint(response.to_json())

        self.assertEqual(type(response.to_json()), dict)

if __name__ == "__main__":
    unittest.main()
