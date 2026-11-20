"""检查本地交换资料的案例是否互相关联。"""
import unittest

from inspect_fixture import read_session


class MaterialTests(unittest.TestCase):
    def test_linked_records(self):
        d = read_session()
        first, correction = d["revisions"][1], d["revisions"][3]
        self.assertEqual(first["tile"], correction["tile"])
        self.assertGreaterEqual(first["edges"][0][2], d["threshold"])
        self.assertLess(correction["edges"][0][2], d["threshold"])
        self.assertIn(first["missing"][0], [row[:2] for row in correction["edges"]])
        self.assertEqual(d["cannot_link"][0][1], d["revisions"][2]["edges"][0][0])
