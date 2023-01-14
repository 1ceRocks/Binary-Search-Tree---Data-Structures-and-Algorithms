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
            
        return elements # it returns all the elements in the tree in specific order [ascending order]
    
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

    
def build_tree(elements):
    print("Building tree with these elements: ", elements)
    # root node for the tree element
    root = BinarySearchTreeNode(elements[0]) 
    
    # building the tree using for loop iteration methods
    for i in range(1, len(elements)):
        root.add_child(elements[i])
        
    return root
 
# return main method with the given data node structure that consist of numbers in list
if __name__ == "__main__":
    countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"] # implementation of sets that contain numbers which are unique and therefore does not allow duplicates.
    country_tree = build_tree(countries) 
    print(country_tree.in_order_traversal()) # call the def in_order_traversal(self) parameter function and executing the code to return the elements with ascending order rule.
    
    """ testing out code block 85 for our binary search tree """
    print("UK is in the list? ", country_tree.search("UK")) # will return True because element 20 exist
    print("Sweden is in the list? ", country_tree.search("Sweden")) # will return False because element 21 does not exist
    print(country_tree.search(200)) # will return False because element 200 does not exist
    
    print(country_tree.in_order_traversal()) # call the def in_order_tra