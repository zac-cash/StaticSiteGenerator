class HTMLNode():
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __repr__(self):
        return f"TextNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if (self.props == None):
            return None 
        output = ""
        for item,value in self.props.items():
            output += f'{item}="{value}" '
        return output.rstrip()
    
