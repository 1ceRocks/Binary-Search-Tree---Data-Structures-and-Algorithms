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
    def add_child(self, data):
        if data == self.data:
            return # binary search tree cannot have duplicate children or elements which are not equal to the current node
        
        if data < self.data:
            # add data in left subtree;
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add data in right subtree;
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    # Implementing an algorithm for specifying a particular order of precedence for a given data node.
    def in_order_traversal(self):
        elements = []
        
        # visiting the left tree element/s
        if self.left:
            # when checking elements = elements plus something, the self.left.in_order_traversal method will return some list and it will add that list to a local "element" list. 
            elements += self.left.in_order_traversal() # calling this function recursively
        
        # visiting the base node
        elements.append(self.data)
        
        # visiting the right tree element/s
        if self.right:
            elements += self.right.in_order_traversal() # ' ' ' '
            
        return elements