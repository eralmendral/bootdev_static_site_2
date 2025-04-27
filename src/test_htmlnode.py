import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode("div", "Hello, World!", None, {"class": "greeting", "style": "color: red;"})
        self.assertEqual(node.props_to_html(), ' class="greeting" style="color: red;"')

    def test_values(self):
        node = HTMLNode("div", "Hello", None, None)
        
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
        
    def test_repr(self):
        node = HTMLNode("p", "Hello", None, {"class": "title"})
        self.assertEqual(node.__repr__(), "HTMLNode(tag='p', value='Hello', children=None, props={'class': 'title'})")
        
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello")
        self.assertEqual(node.to_html(), "<p>Hello</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click Me", {"href": "http://example.com"})
        self.assertEqual(node.to_html(), '<a href="http://example.com">Click Me</a>')
        
    def test_leaf_node_no_tag(self):
        node = LeafNode(None, "Test")
        self.assertEqual(node.to_html(), 'Test')
        
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
        
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")
        
if __name__ == "__main__":
    unittest.main()