import unittest

from textnode import *
from main import *

class TestTextNodeTransformation(unittest.TestCase):

    def test_text_plain_text(self):
        htmlnode = text_node_to_html_node(TextNode("normal text", TextType.TEXT))
        self.assertIsNotNone(htmlnode)
        self.assertIsNone(htmlnode.tag)
        self.assertEqual("normal text", htmlnode.value)
        self.assertIsNone(htmlnode.tag)

    def test_text_bold(self):
        htmlnode = text_node_to_html_node(TextNode("bold text", TextType.BOLD))
        self.assertEqual("b", htmlnode.tag)
        self.assertEqual("bold text", htmlnode.value)

    def test_text_italic(self):
        htmlnode = text_node_to_html_node(TextNode("italic text", TextType.ITALIC))
        self.assertEqual("i", htmlnode.tag)
        self.assertEqual("italic text", htmlnode.value)

    def test_text_code(self):
        htmlnode = text_node_to_html_node(TextNode("code text", TextType.CODE))
        self.assertEqual("code", htmlnode.tag)
        self.assertEqual("code text", htmlnode.value)


    def test_text_link(self):
        htmlnode = text_node_to_html_node(TextNode("link text", TextType.LINK, "link url"))
        self.assertEqual("a", htmlnode.tag)
        self.assertEqual("link text", htmlnode.value)
        self.assertEqual({'href': "link url"}, htmlnode.props)


    def test_text_image(self):
        htmlnode = text_node_to_html_node(TextNode("image text", TextType.IMAGE, "image url"))
        self.assertEqual("img", htmlnode.tag, f"tag for images should be <img> but was {htmlnode.tag}")
        self.assertIsNone(htmlnode.value)
        self.assertEqual("image url", htmlnode.props['src'], f"url of IMG-node should be mapped to property 'src'")
        self.assertEqual("image text", htmlnode.props['alt'], "text of IMG-node should be mapped to property 'alt'")



if __name__ == "__main__":
    unittest.main()
