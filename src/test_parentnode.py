import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class Test_ParentNode(unittest.TestCase):

    def test_init_AssertTagNotEmpty(self):
        msg = "ValueError expected for non-existing tag"
        with self.assertRaisesRegex(ValueError, "tag", msg = msg) as ctx:
            ParentNode(None, None, None)
        msg = "ValueError expected for empty tag"
        with self.assertRaisesRegex(ValueError, "tag", msg = msg) as ctx:
            ParentNode("", None, None)


    def test_init_AssertChildreNotEmpty(self):
        with self.assertRaisesRegex(ValueError, "children", msg = "ValueError expected for non-existing children") as ctx:
            ParentNode("tag", None, None)
        with self.assertRaisesRegex(ValueError, "children", msg = "ValueError expected for non-existing children") as ctx:
            ParentNode("tag", {}, None)

    def test_to_html_simpleTextChild(self):
        node = ParentNode("tag", [LeafNode(None, "text")])
        self.assertEqual("<tag>text</tag>", node.to_html())

    def test_to_html_withProps(self):
        node = ParentNode("tag", [LeafNode("b", None)], {"p1":"v1"})
