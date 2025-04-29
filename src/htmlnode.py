class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props
    self.void_tags = [
      "area",
      "base",
      "br",
      "col",
      "embed",
      "hr",
      "img",
      "input",
      "link",
      "meta",
      "param",
      "source",
      "track",
      "wbr",
      "command",  # HTML5 but less common
      "keygen",   # Deprecated in HTML5 but historically self-closing
      "menuitem"  # Deprecated in HTML5 but historically self-closing
    ]

  def to_html(self):
    raise NotImplementedError

  def props_to_html(self):
    output = ""
    if self.props == None:
      return output
    for key in self.props:
      output += f" {key}=\"{self.props[key]}\""
    return output

  def __repr__(self):
    return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
  def __init__(self, tag, value, props=None):
    super().__init__(tag, value, None, props)

  def to_html(self):
    if self.value == None:
      raise ValueError("error: missing value")
    if self.tag == None:
      return self.value
    if self.tag in self.void_tags:
      return f"<{self.tag}{self.props_to_html()}>{self.value}"
    return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None):
    super().__init__(tag, None, children, props)

  def to_html(self):
    if self.tag is None:
      raise ValueError("error: missing tag")
    if self.children is None:
      raise ValueError("error: missing children")
    children_html = ""
    for child in self.children:
      children_html += child.to_html()

    if self.tag in self.void_tags:
      return f"<{self.tag}{self.props_to_html()}{children_html}>"
    return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
