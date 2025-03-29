import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):

    def test_to_html(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

        node = LeafNode("button", "Press me!", {"disabled": "true"})
        self.assertEqual(node.to_html(), '<button disabled="true">Press me!</button>')


if __name__ == "__main__":
    unittest.main()
