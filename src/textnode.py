class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, othernode):
        if (
            self.text == othernode.text
            and self.text_type == othernode.text_type
            and self.url == othernode.url
        ): return True

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

        

