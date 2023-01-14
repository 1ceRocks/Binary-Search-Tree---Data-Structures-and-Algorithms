# PYTHON BINARY SEARCH TREE
# DATA STRUCTURES AND ALGORITHMS
# BSCOE 2-6 (2022-2023) -- GITHUB
# 1/14/2023

"""
    Source Code: https_://www.youtube.com/watch?v=lFq5mYUWEBk
                 https_://www.youtube.com/watch?v=JnrbMQyGLiU
                 
    Create a demo using the letters in your fullname as the content of the binary tree.
Upload all source code in new github repository.
"""

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, data):
        if data ==self.data:
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