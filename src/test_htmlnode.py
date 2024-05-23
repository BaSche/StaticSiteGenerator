import unittest
from htmlnode import HTMLNode

class Test_HTMLNode(unittest.TestCase):

    def test_init_AssertValueOrChildren(self):
        with self.assertRaises(ValueError, msg = "ValueError expected iof value and children are None"):
            HTMLNode(None, None, None, None) 

        with self.assertRaises(ValueError, msg = "ValueError expected if no value and children are empty"):
            HTMLNode(None, "", (), None)

    def test_repr(self):
        node = HTMLNode("tag", "value", (), {})
        self.assertEqual(
                "HTMLNode(tag, value)",
                "" + node.__repr__())

    def test_props_to_html_EmptyProps(self):
        node = HTMLNode("tag", "value", None, {})
        self.assertEqual("", node.props_to_html(), "empty props must be rendered as empty string")

    def test_props_to_html(self):
        node = HTMLNode("tag", "value", None, {"p1" : "v1", "p2" : "v2"})
        self.assertEqual('p1="v1" p2="v2"', node.props_to_html())
