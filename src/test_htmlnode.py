import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

class TestParentNode(unittest.TestCase):
  def test_to_html_no_children(self):
    with self.assertRaises(ValueError):
      node = ParentNode("p", None)
      node.to_html()

  def test_to_html_no_tag(self):
    with self.assertRaises(ValueError):
      child_node = LeafNode("p", "child")
      parent_node = ParentNode(None, child_node)
      parent_node.to_html()

  def test_to_html_empty(self):
    with self.assertRaises(ValueError):
      node = ParentNode(None, None)
      node.to_html()

  def test_to_html_with_children(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

  def test_to_html_with_grandchildren(self):
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(
      parent_node.to_html(),
      "<div><span><b>grandchild</b></span></div>",
                     )

  def test_to_html_multiple_children(self):
    child_node1 = LeafNode("span", "child1")
    child_node2 = LeafNode("span", "child2")
    parent_node = ParentNode("div", [child_node1, child_node2])
    self.assertEqual(
      parent_node.to_html(),
      "<div><span>child1</span><span>child2</span></div>"
      )

  def test_to_html_multiple_grandchildren(self):
    grandchild_node1 = LeafNode("p", "grandchild1")
    grandchild_node2 = LeafNode("p", "grandchild2")
    child_node = ParentNode("span", [grandchild_node1, grandchild_node2])
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(
      parent_node.to_html(),
      "<div><span><p>grandchild1</p><p>grandchild2</p></span></div>"
      )

  def test_to_html_props(self):
    child_node = LeafNode("p", "Hello")
    parent_node = ParentNode("div", [child_node], {"class": "container", "id": "main"})
    self.assertEqual(parent_node.to_html(), "<div class=\"container\" id=\"main\"><p>Hello</p></div>")

  def test_to_html_empty_children_list(self):
    node = ParentNode("div", [])
    self.assertEqual(node.to_html(), "<div></div>")

  def test_to_html_mixed_nodes(self):
    node = ParentNode(
    "section",
    [
        LeafNode("h1", "Title"),
        ParentNode("div", [LeafNode("p", "Paragraph")]),
        LeafNode("footer", "Copyright")
    ]
    )
    self.assertEqual(node.to_html(), "<section><h1>Title</h1><div><p>Paragraph</p></div><footer>Copyright</footer></section>")

if __name__ == "__main__":
  unittest.main()
