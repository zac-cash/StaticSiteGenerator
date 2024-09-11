import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        testcases = [
            (
                LeafNode("a", "Click me!", {"href": "https://www.google.com"}),
                '<a href="https://www.google.com">Click me!</a>'
            ),
            (
                LeafNode("p", "This is a paragraph of text."),
                '<p>This is a paragraph of text.</p>'
            ),
            (
                LeafNode(tag="p", value="This is a paragraph of text."),
                '<p>This is a paragraph of text.</p>'
            ),            
            (
                LeafNode(value="This is a paragraph of text."),
                'This is a paragraph of text.'
            ),
            (
                LeafNode(value="This is a paragraph of text.",tag="p",props={"href": "https://www.google.com","target": "_blank"}),
                '<p href="https://www.google.com" target="_blank">This is a paragraph of text.</p>'
            )
        ]
        not_equal_testcases = [
            (
                LeafNode("Click me!","a", {"href": "https://www.google.com"}),
                '<a href="https://www.google.com">Click me!</a>'
            )
        ]
        assert_testcases = [
            (
                LeafNode(tag="p"),
                ValueError
            )
        ]

        for node,expected in testcases:
            #print(node)
            self.assertEqual(node.to_html(),expected)

        for node,expected in not_equal_testcases:
            #print(node)
            self.assertNotEqual(node.to_html(),expected)
        
        for node,exception in assert_testcases:
            with self.assertRaises(exception):
                self.assertIsNone(node.to_html())

if __name__ == "__main__":
    unittest.main()