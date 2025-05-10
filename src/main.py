from textnode import TextType
from textnode import TextNode
from leafnode import LeafNode

def main():
    node = TextNode("hello world", TextType.TEXT, "www.example.org")
    print(node)

def text_node_to_html_node(text_node):
    tag = None
    props = None
    if text_node.text_type == TextType.BOLD:
        tag = "b"
    elif text_node.text_type == TextType.ITALIC:
        tag = "i"
    elif text_node.text_type == TextType.CODE:
        tag = "code"
    elif text_node.text_type == TextType.LINK:
        tag = "a"
        props = {'href': text_node.url}
        
    return LeafNode(tag, text_node.text, props)

main()
