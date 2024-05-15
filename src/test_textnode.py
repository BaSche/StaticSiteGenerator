import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_repr(self):
        node= TextNode("text", "type", "url")
        self.assertEqual(
                "TextNode(text, type, url)",
                node.__repr__())

    def test_repr_none(self):
        node = TextNode(None, None, None)
        self.assertEqual(
                "TextNode(None, None, None)",
                node.__repr__())

    def test_eq(self):
        node1 = TextNode("text", "type", "url")
        node2 = TextNode("text", "type", "url")

        self.assertEqual(node1, node2)

    def test_eq_empty(self):
        node1 = TextNode("", "", "")
        node2 = TextNode("", "", "")

        self.assertEqual(node1, node2)

    def test_eq_not_text(self):
        node1 = TextNode("one", "type", "url")
        node2 = TextNode("two", "type", "url")

        self.assertNotEqual(node1, node2)

    def test_eq_not_type(self):
        node1 = TextNode("text", "type_one", "url")
        node2 = TextNode("text", "type_two", "url")

        self.assertNotEqual(node1, node2)

    def test_eq_not_url(self):
        node1 = TextNode("text", "type", "one")
        node2 = TextNode("text", "type", "two")

        self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()
