import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

        node = HTMLNode(props={"foo": "foo_val"})
        self.assertEqual(node.props_to_html(), ' foo="foo_val"')

        node = HTMLNode(props={"foo": "foo_val", "bar": "bar_val"})
        self.assertEqual(node.props_to_html(), ' foo="foo_val" bar="bar_val"')

    def test_repr(self):
        node = HTMLNode("h1", "Hello World!", [HTMLNode("div")], {"foo": "foo_val"})
        self.assertEqual(
            repr(node),
            "HTMLNode(h1, Hello World!, [HTMLNode(div, None, None, None)], {'foo': 'foo_val'})",
        )


if __name__ == "__main__":
    unittest.main()
