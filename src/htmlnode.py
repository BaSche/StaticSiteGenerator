class HTMLNode:
    def __init__(self,
            tag=None,
            value=None,
            children=None,
            props=None
            ):

        if not value and not children:
            raise ValueError("either value or children are needed")
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def props_to_html(self):
        if not self.props:
            return ""
        propsAsHTML = list()
        for p in self.props:
            propsAsHTML.append(f' {p}="{self.props[p]}"')
        return "".join(propsAsHTML)

    def to_html(self):
        raise NotImplementedError

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value})"

