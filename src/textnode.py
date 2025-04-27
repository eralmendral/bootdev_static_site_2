from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
  NORMAL = "Normal text"
  BOLD = "**Bold text**"
  ITALIC = "_Italic text_"
  CODE = "`Code text`"
  LINK = "[anchor text](url)"
  IMAGE = "![alt text](url)"


class TextNode:
  def __init__(self, text, text_type, url=None):
    self.text = text
    self.text_type = text_type
    self.url = url

  def render(self):
    return self.text

  def __eq__(self, other):
    return (
      self.text == other.text
      and self.text_type == other.text_type
      and self.url == other.url
    )
  
  def __repr__(self):
    return f"TextNode(text={self.text}, text_type={self.text_type.value}, url={self.url})"
  
  def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
      raise ValueError(f"Invalid text_type: {text_node.text_type}")
    
    if text_node.text_type == TextType.NORMAL:
      return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
      return LeafNode("strong", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
      return LeafNode("em", text_node.text)
    elif text_node.text_type == TextType.CODE:
      return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
      return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
      return LeafNode("img", None, {"src": text_node.url, "alt": text_node.text})