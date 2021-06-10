#Name: Terry Su
#Date: June 5, 2021
#Purpose: Building an unbalanced binary search tree + some methods from scratch 

class Node:

    #constructor for each node in the BST
    def __init__(self, value = None, left=None, right = None): #None is like null
        self.value = value
        self.left = left
        self.right = right

class BST:

    #left child node always < parent node
    #right child node always > parent node

    def __init__(self,root = None):
        self.root = root

    def insert(self,value):
        
        spot = self.root
        new_node = Node(value)

        if self.root == None:
            self.root = new_node
            return
        
        while True: #until according empty spot is found (spot.left or spot.right)
            if value > spot.value: #going right
                
                if spot.right == None:
                    spot.right = new_node
                    return

                else:
                    spot = spot.right

            elif value < spot.value: #going left

                if spot.left == None:
                    spot.left = new_node
                    return

                else:
                    spot = spot.left

            elif value == spot.value: #special case if value inserted already exists
                return 

    def lookup(self,value):
        
        spot = self.root
        
        while spot != None: #traverse tree according to rules
            if value > spot.value:
                spot = spot.right

            elif value < spot.value:
                spot = spot.left

            elif value == spot.value:
                return spot

        return print(value, 'was not found')


root = Node(5)
tree = BST(root)
tree.insert(4)
tree.insert(3)
tree.insert(6)
tree.lookup(9)
print(tree.root.left.left.value)
