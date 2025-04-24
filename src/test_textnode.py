import unittest

from textnode import TextNode
from textnode import TextType


class TestTextNode(unittest.TestCase):

    def test_texttype_valueerror (self):
        with self.assertRaises(ValueError, msg = ""):
            node = TextNode("text", "no Texttype", None)
        

    def test_repr(self):
        node= TextNode("text")
        self.assertEqual(
                "TextNode(text, TextType.NORMAL, None)",
                node.__repr__())

    def test_repr_none(self):
        node = TextNode(None)
        self.assertEqual(
                "TextNode(None, TextType.NORMAL, None)",
                node.__repr__())

    def test_eq(self):
        node1 = TextNode("text", TextType.CODE, "url")
        node2 = TextNode("text", TextType.CODE, "url")

        self.assertEqual(node1, node2)

    def test_eq_empty(self):
        node1 = TextNode("")
        node2 = TextNode("")

        self.assertEqual(node1, node2)

    def test_eq_not_text(self):
        node1 = TextNode("one", TextType.NORMAL, "url")
        node2 = TextNode("two", TextType.NORMAL, "url")

        self.assertNotEqual(node1, node2)

    def test_eq_not_type(self):
        node1 = TextNode("text", TextType.LINK, "url")
        node2 = TextNode("text", TextType.IMAGE, "url")

        self.assertNotEqual(node1, node2)

    def test_eq_not_url(self):
        node1 = TextNode("text", TextType.CODE, "one")
        node2 = TextNode("text", TextType.CODE, "two")

        self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()
