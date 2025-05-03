import unittest

from parsemd import split_nodes_delimiter as snd

from textnode import TextNode

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(snd([TextNode("", "")], "", ""), None)

    def test_string(self):
        self.assertEqual(snd([TextNode("This is a string", "")], "", ""), "This is a string")
