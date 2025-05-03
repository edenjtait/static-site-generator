from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
  result = []

  for old_node in old_nodes:
    if old_node.text_type is not TextType.TEXT:
      result.append(old_node)
      continue

    current_text = old_node.text

    while True:
      first_pos = current_text.find(delimiter)
      if first_pos == -1:
        if current_text:
          result.append(TextNode(current_text, TextType.TEXT))
        break

      second_pos = current_text.find(delimiter, first_pos + len(delimiter))
      if second_pos == -1:
        raise ValueError("closing delimiter '{delimiter}' not found")

      delimiter_len = len(delimiter)

      before_text = current_text[:first_pos]

      middle_text = current_text[first_pos + delimiter_len:second_pos]

      after_text = current_text[second_pos + delimiter_len:]

      if before_text:
        result.append(TextNode(before_text, TextType.TEXT))

      result.append(TextNode(middle_text, text_type))

      current_text = after_text
