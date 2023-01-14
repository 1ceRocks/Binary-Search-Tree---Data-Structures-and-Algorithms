# Exercise Reference Source Link: https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/8_Binary_Tree_1/8_binary_tree_part_1_exercise.md

# * REQUIRED TERMINAL OUTPUT
""" find_min(): finds minimum element in entire binary tree
    find_max(): finds maximum element in entire binary tree
    calculate_sum(): calculates sum of all elements
    post_order_traversal(): performs post order traversal of a binary tree
    pre_order_traversal(): performs pre order traversal of a binary tree\
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
    
    def search(self, val):
        if self.data == val:
            return True
        
        # if the value we're searching for is less than data
        if val < self.data:
            if self.left:
                return self.left.search(val) # it will do a recursive search on the left subtree and is the same function as above
            else:
                return False # when it reach to end, it indicates that this does not exist in our tree
            # 'val' might be in left subtree (not guaranteed)
            
        # if the value we're searching for is greater than data
        if val > self.data:
            if self.right:
                return self.right.search(val) # it will do a recursive search
            else:
                return False
            # 'val' might be in right subtree (not guaranteed)

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
            
        return elements # it returns all the elements in the tree in specific order [ascending order]
    
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
    
    def calculate_sum(self):
        if self.left:
            left_sum = self.left.calculate_sum()
        else:
            left_sum = 0
            
        if self.right:
            right_sum = self.right.calculate_sum()
        else:
            right_sum = 0
        
        return self.data + left_sum + right_sum
    
def build_tree(elements):
    print("\nBuilding tree with these elements: ", elements)
    # root node for the tree element
    root = BinarySearchTreeNode(elements[0]) 
    
    # building the tree using for loop iteration methods
    for i in range(1, len(elements)):
        root.add_child(elements[i])
        
    return root
 
# return main method with the given data node structure that consist of numbers in list
if __name__ == "__main__":
    numbers = [23, 3, 1, 27, 13, 8, 17, 60]
    
    numbers_tree = build_tree(numbers)
    
    print("\nInput numbers: ", numbers)
    print("Minimum number: ", numbers_tree.find_min())
    print("Maximum number: ", numbers_tree.find_max())
    print("Calculated sum: ", numbers_tree.calculate_sum())
    print("\nPre Order Traversal: ", numbers_tree.pre_order_traversal())
    print("Post Order Traversal: ", numbers_tree.post_order_traversal())