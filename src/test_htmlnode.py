import unittest

from htmlnode import HTMLNode



class TestHTMLNode(unittest.TestCase):
    def test_none(self):
        nodelist = []
        nodelist.append(HTMLNode(tag="hi", value=None, children="a child"))
        nodelist.append(HTMLNode())
        nodelist.append(HTMLNode("hello","hi","hello",None))

        for test_node in nodelist:
            self.assertIsNone(test_node.props)

    def test_raise(self):
        nodelist = []
        nodelist.append(HTMLNode(tag="hi", value=None, children="a child"))
        nodelist.append(HTMLNode())
        nodelist.append(HTMLNode("hello","hi","hello",None))

        with self.assertRaises(NotImplementedError):
            for test_node in nodelist:
                self.assertIsNone(test_node.to_html())

    def test_props_to_html(self):
        testcases = [
            (
                HTMLNode(
                tag="hi",
                value=None,
                children="a child",
                props={"href": "https://www.google.com","target": "_blank"}
                ),
                ' href="https://www.google.com" target="_blank"'
            ),
            (
                HTMLNode(),
                None
            ),
        ]
        neg_testcases = [
            (
                HTMLNode(
                tag="hi",
                value=None,
                children="a child",
                props={"href": "https://www.google.com","target": "_blank"}
                ),
                ' hrf="https://www.google.com" target="_blank"'
            ),
            (
                HTMLNode(props={"href": "https://www.google.com","target": "_blank"}),
                None
            ),
        ]

        for node,expected in testcases:
            self.assertEqual(node.props_to_html(),expected)

        for node,expected in neg_testcases:
            self.assertNotEqual(node.props_to_html(),expected)

if __name__ == "__main__":
    unittest.main()