class HTMLNode:
  def __init__(self, tag, value, children, props):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props
    
  def to_html(self):
    raise NotImplementedError("Subclasses must implement the to_html method.")

  def props_to_html(self):
    if self.props is None:
        return ''
    return ''.join(f' {key}="{value}"' for key, value in self.props.items())

  def __repr__(self):
    return f"HTMLNode(tag={self.tag!r}, value={self.value!r}, children={self.children!r}, props={self.props!r})"
  

class LeafNode(HTMLNode):
  def __init__(self, tag,  value, props=None):
    super().__init__(tag, value, None, props)
  
  def to_html(self):
    if self.value == None:
        raise ValueError("LeafNode value cannot be None")
    if self.tag == None:
        return self.value
    return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
  
  def __repr__(self):
    return f"LeafNode({self.tag}, {self.value}, {self.props})"
  
  
class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None):
    super().__init__(tag, None, children, props)
  
  def to_html(self):
    if self.tag == None:
      raise ValueError("ParentNode tag cannot be None")
    if self.children == None:
      raise ValueError("ParentNode children cannot be None")
    
    children_html = ''.join(child.to_html() for child in self.children)
    return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    
  

