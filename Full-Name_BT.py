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
                
    def search(self, val):
        if self.data == val:
            return True
        
        # if the value we're searching for is less than data
        if val < self.data:
            if self.left:
                return self.left.search(val) # it will do a recursive search on the left subtree and is the same function as above
            else:
                return False # when it reach to end, it indicates that this does not exist in subtree
            # 'val' might be in left subtree (not guaranteed)
        
        # if the value we're searching for is greater than data
        if val > self.data:
            if self.right:
                return self.right.search(val) # it will do a recursive search
            else:
                return False
            # 'val' might be in left subtree (not guaranteed)
            
    # Implementing an algorithm for specifying a particular order of precedence for a given data node.
    def in_order_traversal(self):
        elements = []
        
        # visiting the left element/s
        if self.left:
            # when checking elements = elements plus something, then self.left.in_order_traversal() method will return some list and it will add that list to a local "element" list.
            elements += self.left.in_order_traversal() # calling this function recursively
            
        # visiting the base node
        elements.append(self.data)
        
        # visiting the right tree element/s
        if self.right:
            elements += self.right.in_order_traversal() # ' ' ' '
            
        return elements # it returns all the elements in the tree in specified order [ascending order]
    
    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
            
        return elements
    
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
            
        elements.append(self.data) 
            
        return elements
    
    def find_min(self):
        if self.left is None: # the left child element of the root node has been used as the perspective view for finding the minimum element in the binary tree.
            return self.data
        return self.left.find_min()
    
    def find_max(self):
        if self.right is None: # the right child element of the root node has been used as the perspective view for finding the minimum element in the binary tree.
            return self.data
        return self.right.find_max()
    
    def delete(self, val): # implementing delete function where we can supply a particular value and it will delete the node from the binary tree
        if val < self.data: # checking if the value is less than the self.data
            if self.left:
                self.left = self.left.delete(val) # recursively call delete method on the left subtree
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        
        else:
            if self.left is None and self.right is None: # we raised the last data point, left and right subtree is basically None
                return None
            """
                recursion method
            """
            if self.left is None: # we have right but we don't have left subtree
                return self.right
            if self.right is None:
                return self.right
            
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)
            
        return self