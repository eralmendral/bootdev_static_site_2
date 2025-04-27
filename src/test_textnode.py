import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_text_type_different(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.NORMAL)
        self.assertNotEqual(node, node2)
        
    def test_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertIsNone(node.url)
        
    def test_text(self):
        node = TextNode("Hello", TextType.NORMAL)
        html_node = node.text_node_to_html_node()
        self.assertEqual(node.text, "Hello")
        self.assertEqual(html_node.value, "Hello")


if __name__ == "__main__":
    unittest.main()
