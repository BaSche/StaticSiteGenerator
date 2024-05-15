import unittest
from htmlnode import HTMLNode

class Test_HTMLNode(unittest.TestCase):

    
    def test_repr(self):
        node = HTMLNode("tag", "value", (), {})
            
