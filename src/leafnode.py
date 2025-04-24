from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        if not tag and not value:
            raise ValueError("value may not be None")
        if not tag and props != None and len(props):
            raise ValueError("tag may not be None if props are given")
            
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.tag:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        else:
            return self.value
