import unittest
from leafnode import LeafNode

class Test_LeafNode(unittest.TestCase):

    def test_init_empty_tag(self):
        with self.assertRaises(ValueError, msg = "ValueError expected if value and tag are empty"):
            node = LeafNode(None, None, None)

        with self.assertRaises(ValueError, msg = "ValueError expected if tag is empty, but props are not"):
            node = LeafNode(None, "value", {'p1':'v1', 'p2':'v2'})


    def test_init(self):
        node = LeafNode("p", "paragraph", None)

    def test_to_html_value(self):
        self.assertEqual("value", LeafNode(None, "value").to_html())

    def test_to_html_tag(self):
        self.assertEqual("<tag>value</tag>", LeafNode("tag", "value").to_html())

    def test_to_html_props(self):
        self.assertEqual('<t p1="v1">value</t>', LeafNode("t", "value", {'p1':'v1'}).to_html())
