from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        if not tag:
            raise ValueError('tag is not allowed to be empty')
        if not children:
            raise ValueError('children is not allowed to be empty')
        self.tag = tag
        self.children = children


    def to_html(self):
        tokens = [f"<{self.tag}>"]
        for child in self.children:
            tokens.append(child.to_html())
        tokens.append(f"</{self.tag}>")
        return "".join(tokens)
