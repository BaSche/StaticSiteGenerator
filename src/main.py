from textnode import TextType
from textnode import TextNode
from leafnode import LeafNode

def main():
    node = TextNode("hello world", TextType.NORMAL, "www.example.org")
    print(node)

def text_node_to_html_node(text_node):
    return LeafNode(None, "leaf")

main()
