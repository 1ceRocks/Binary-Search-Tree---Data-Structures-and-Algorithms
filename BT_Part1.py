"""Implementation of Binary Search Tree"""

"""A general tree where a node can have any number of element/children

    Binary Tree = max of 2 elements
    
    Binary Search Tree = with a specific order where left search tree has all the elements which is less than the current node and the right search has all the greater elements than the root node.
"""

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    # this could be a root node or any node on the tree
    # supplementing 'data' as a parameter for the add_child
    def add_child(self, data):
    #TODO: we first need to check the value of our 'data';