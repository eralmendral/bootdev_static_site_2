from block_markdown import (markdown_to_blocks, block_to_block_type, BlockType)

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