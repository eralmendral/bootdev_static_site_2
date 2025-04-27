from textnode import TextNode, TextType
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
  new_nodes = []
  for old_node in old_nodes:
    if old_node.text_type != TextType.TEXT:
      new_nodes.append(old_node)
      continue
    split_nodes = []
    sections = old_node.text.split(delimiter)
    if len(sections) % 2 == 0:
      raise ValueError("invalid markdown")
    for i in range(len(sections)):
      if sections[i] == "":
        continue
      if i % 2 == 0:
        split_nodes.append(TextNode(sections[i], TextType.TEXT))
      else:
        split_nodes.append(TextNode(sections[i], text_type))
    new_nodes.extend(split_nodes)
    
  return new_nodes

def extract_markdown_images(text):
  pattern = r"!\[([^\]]*)\]\(([^)]+)\)"
  matches = re.findall(pattern, text)
  return matches

def extract_markdown_links(text):
  pattern = r"\[([^\]]+)\]\(([^)]+)\)"
  matches = re.findall(pattern, text)
  return matches

def split_nodes_image(old_nodes):
  new_nodes = []
  for old_node in old_nodes:
    if old_node.text_type != TextType.TEXT:
      new_nodes.append(old_node)
      continue
    split_nodes = []
    text = old_node.text
    matches = extract_markdown_images(text)
    last_index = 0
    for alt_text, url in matches:
      start_index = text.find(f"![{alt_text}]({url})", last_index)
      if start_index > last_index:
        split_nodes.append(TextNode(text[last_index:start_index], TextType.TEXT))
      split_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
      last_index = start_index + len(f"![{alt_text}]({url})")
    if last_index < len(text):
      split_nodes.append(TextNode(text[last_index:], TextType.TEXT))
    new_nodes.extend(split_nodes)

  return new_nodes


def split_nodes_link(old_nodes):
  new_nodes = []
  for old_node in old_nodes:
    if old_node.text_type != TextType.TEXT:
      new_nodes.append(old_node)
      continue
    split_nodes = []
    text = old_node.text
    matches = extract_markdown_links(text)
    last_index = 0
    for link_text, url in matches:
      start_index = text.find(f"[{link_text}]({url})", last_index)
      if start_index > last_index:
        split_nodes.append(TextNode(text[last_index:start_index], TextType.TEXT))
      split_nodes.append(TextNode(link_text, TextType.LINK, url))
      last_index = start_index + len(f"[{link_text}]({url})")
    if last_index < len(text):
      split_nodes.append(TextNode(text[last_index:], TextType.TEXT))
    new_nodes.extend(split_nodes)

  return new_nodes

def text_to_textnodes(text):
  nodes = [TextNode(text, TextType.TEXT)]
  nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
  nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
  nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
  nodes = split_nodes_image(nodes)
  nodes = split_nodes_link(nodes)
  return nodes