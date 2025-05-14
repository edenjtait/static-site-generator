import unittest

from parsemd import split_nodes_delimiter as snd

from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(snd([TextNode("", "")], "", ""), None)

    def test_string(self):
        node = TextNode("This is a string", TextType.TEXT)
        new_node = snd([node], None, TextType.TEXT)
        self.assertEqual(new_node, "something")
