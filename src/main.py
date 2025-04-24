from textnode import TextType
from textnode import TextNode
def main():
    node = TextNode("hello world", TextType.NORMAL, "www.example.org")
    print(node)

main()
