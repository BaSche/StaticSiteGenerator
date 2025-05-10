import unittest

from main import text_node_to_html_node

class TestTextNodeTransformation(unittest.TestCase):

    def text_plain_text(self):
        htmlnode = text_node_to_html_node(TextNode(None, "normal text"))
        self.assertIsNotNone(htmlnode)
        self.assertIsNone(htmlnode.tag)
        self.assertEqual("normal text", htmlnode.value)

if __name__ == "__main__":
    unittest.main()
