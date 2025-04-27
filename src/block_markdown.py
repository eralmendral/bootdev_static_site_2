from enum import Enum
from htmlnode import HTMLNode

class BlockType(Enum):
  PARAGRAPH = "paragraph"
  HEADING = "heading"
  CODE = "code"
  QUOTE = "quote"
  UNORDERED_LIST = "unordered_list"
  ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
  if block.startswith("#"):
    parts = block.split(" ", 1)
    if len(parts) > 1 and parts[0].count("#") <= 6 and parts[0] == "#" * len(parts[0]):
      return BlockType.HEADING
  elif block.startswith("```") and block.endswith("```"):
    return BlockType.CODE
  elif all(line.startswith(">") for line in block.splitlines()):
    return BlockType.QUOTE
  elif all(line.startswith("- ") for line in block.splitlines()):
    return BlockType.UNORDERED_LIST
  elif all(line.split(". ", 1)[0].isdigit() and line.startswith(f"{i}. ") for i, line in enumerate(block.splitlines(), start=1)):
    return BlockType.ORDERED_LIST
  else:
    return BlockType.PARAGRAPH


def markdown_to_blocks(markdown):
  blocks = markdown.split("\n\n")
  blocks = [block.strip() for block in blocks if block.strip()]
  return blocks 


def markdown_to_html_node(markdown):
  root = HTMLNode("div")
  blocks = markdown_to_blocks(markdown)
  
  for block in blocks:
    block_type = block_to_block_type(block)
    
    if block_type == BlockType.HEADING:
      level = block.split(" ", 1)[0].count("#")
      content = block.split(" ", 1)[1]
      root.add_child(HTMLNode(f"h{level}", content))
    
    elif block_type == BlockType.PARAGRAPH:
      root.add_child(HTMLNode("p", block))
    
    elif block_type == BlockType.CODE:
      content = block.strip("```")
      root.add_child(HTMLNode("pre", HTMLNode("code", content)))
    
    elif block_type == BlockType.QUOTE:
      quote_content = "\n".join(line.lstrip("> ") for line in block.splitlines())
      root.add_child(HTMLNode("blockquote", quote_content))
    
    elif block_type == BlockType.UNORDERED_LIST:
      ul_node = HTMLNode("ul")
      for line in block.splitlines():
        ul_node.add_child(HTMLNode("li", line.lstrip("- ")))
      root.add_child(ul_node)
    
    elif block_type == BlockType.ORDERED_LIST:
      ol_node = HTMLNode("ol")
      for line in block.splitlines():
        content = line.split(". ", 1)[1]
        ol_node.add_child(HTMLNode("li", content))
      root.add_child(ol_node)
  
  return root