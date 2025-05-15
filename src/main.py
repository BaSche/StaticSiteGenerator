from textnode import TextType
from textnode import TextNode
from leafnode import LeafNode

def main():
    node = TextNode("hello world", TextType.TEXT, "www.example.org")
    print(node)

def text_node_to_html_node(text_node):
    tag = None
    text = text_node.text
    props = {}
    if text_node.text_type == TextType.BOLD:
        tag = "b"
    elif text_node.text_type == TextType.ITALIC:
        tag = "i"
    elif text_node.text_type == TextType.CODE:
        tag = "code"
    elif text_node.text_type == TextType.LINK:
        tag = "a"
        props['href'] = text_node.url
    elif text_node.text_type == TextType.IMAGE:
        tag = "img"
        text = None
        props['alt'] = text_node.text
        props['src'] = text_node.url
        
    return LeafNode(tag, text, props)

if __name__ == "__main__":
    main()
