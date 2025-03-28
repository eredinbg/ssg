import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_init(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.text, "This is a text node")
        self.assertEqual(node.text_type, TextType.BOLD)
        self.assertIsNone(node.url)

        node = TextNode("This is a text node", TextType.LINK, "https://example.com")
        self.assertEqual(node.text, "This is a text node")
        self.assertEqual(node.text_type, TextType.LINK)
        self.assertEqual(node.url, "https://example.com")

    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        node3 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node, node3)

        node4 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node4)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, None)")


if __name__ == "__main__":
    unittest.main()
