from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self,tag=None,value=None,props=None):
        #if (not hasattr(self,"value")):
        #    raise ValueError(f"{self.__repr__} - no value!")
        #if hasattr(self,"children"):
        #    raise ValueError(f"{self.__repr__} - no children allowed value!")
        #
        super().__init__(tag=tag,value=value,children=None,props=props)
    
    def __repr__(self):
        return f"value={self.value},tag={self.tag},props={self.props}"
    
    def to_html(self):
        if (self.value is None):
            raise ValueError(f"{self.__repr__} - no value!")
        if (self.tag == None):
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
