from enum import Enum

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