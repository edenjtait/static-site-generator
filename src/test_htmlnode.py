import unittest

from htmlnode import HTMLNode, LeafNode

class TestHtmlNode(unittest.TestCase):

  def test_props_to_html_empty(self):
    node = HTMLNode(props=None)
    self.assertEqual(node.props_to_html(), "")

  def test_props_to_html_single(self):
    node = HTMLNode(props={"href": "https://boot.dev"})
    self.assertEqual(node.props_to_html(), " href=\"https://boot.dev\"")

  def test_props_to_html_multiple(self):
    node = HTMLNode(props={"href": "https://boot.dev", "target": "_blank"})
    self.assertEqual(node.props_to_html(), " href=\"https://boot.dev\" target=\"_blank\"")

  def test_repr(self):
    node = HTMLNode("div", "content", [], {"class": "container"})
    self.assertIn("div", repr(node))
    self.assertIn("content", repr(node))

class TestLeafNode(unittest.TestCase):
  def test_leaf_to_html(self):
    node = LeafNode("p", "Hello, world!")
    self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

  def test_leaf_to_html_link(self):
    node = LeafNode("a", "Click me!", {"href": "https://boot.dev"})
    self.assertEqual(node.to_html(), "<a href=\"https://boot.dev\">Click me!</a>")

  def test_leaf_to_html_no_tag(self):
    node = LeafNode(None, "This should go round and round")
    self.assertEqual(node.to_html(), "This should go round and round")

  def test_leaf_to_html_no_value(self):
    with self.assertRaises(ValueError):
      node = LeafNode("p", None)
      node.to_html()

  def test_leaf_to_html_empty_value(self):
    node = LeafNode(None, "")
    self.assertEqual(node.to_html(), "")

  def test_leaf_to_html_void_tags(self):
    node = LeafNode("img", "", {"src": "bear.png", "alt": "A wise wizard bear"})
    self.assertEqual(node.to_html(), "<img src=\"bear.png\" alt=\"A wise wizard bear\">")

if __name__ == "__main__":
  unittest.main()
