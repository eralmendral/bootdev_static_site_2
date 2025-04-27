from block_markdown import (markdown_to_blocks, block_to_block_type, markdown_to_html_node, BlockType)
from gencontent import extract_title

def test_markdown_to_blocks(self):
    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
    blocks = markdown_to_blocks(md)
    self.assertEqual(
        blocks,
        [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ],
    )

def test_block_to_block_type(self):
    self.assertEqual(block_to_block_type("This is a paragraph"), BlockType.PARAGRAPH)
    self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
    self.assertEqual(block_to_block_type("## Heading 2"), BlockType.HEADING)
    self.assertEqual(block_to_block_type("```\ncode block\n```"), BlockType.CODE)
    self.assertEqual(block_to_block_type("> This is a quote\n> Another line"), BlockType.QUOTE)
    self.assertEqual(block_to_block_type("- Item 1\n- Item 2"), BlockType.UNORDERED_LIST)
    self.assertEqual(block_to_block_type("1. First item\n2. Second item"), BlockType.ORDERED_LIST)
    
    
def test_paragraphs(self):
    md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

def test_codeblock(self):
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )
    
    
def test_extract_title(self):
    md = """
# This is a title
This is a paragraph.
"""
    title = extract_title(md)
    self.assertEqual(title, "This is a title")
    md = """
# Another title
This is another paragraph.
"""
    title = extract_title(md)
    self.assertEqual(title, "Another title")
    md = """
# Title with multiple lines
This is a paragraph.
"""
    title = extract_title(md)
    self.assertEqual(title, "Title with multiple lines")
    md = """
# Title with multiple lines and extra spaces
This is a paragraph.
"""
    title = extract_title(md)
    self.assertEqual(title, "Title with multiple lines and extra spaces")
    md = """
# Title with multiple lines and extra spaces
This is a paragraph.
"""
    title = extract_title(md)
    self.assertEqual(title, "Title with multiple lines and extra spaces")
    