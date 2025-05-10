from enum import Enum

class TextType(Enum):
    NORMAL  = 0
    BOLD    = 1
    ITALIC  = 2
    CODE    = 3
    LINK    = 4
    IMAGE   = 5

class TextNode:
    text = ""
    text_type = ""
    url = ""

    def __init__(self, text, text_type = TextType.NORMAL, url = None):
        if not (isinstance(text_type, TextType)):
            raise ValueError(f"Texttype expected. Found instead: {text_type}")
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text\
            and self.text_type == other.text_type\
            and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

