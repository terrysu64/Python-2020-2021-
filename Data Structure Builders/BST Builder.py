#Name: Terry Su
#Date: June 5, 2021
#Purpose: Building an unbalanced binary search tree + some methods from scratch 

class Node:

    #constructor for each node in the BST
    def __init__(self, testue = None, left=None, right = None): #None is like null
        self.testue = testue
        self.left = left
        self.right = right

class BST:

    #left child node always < parent node
    #right child node always > parent node

    def __init__(self,root = None):
        self.root = root

    def insert(self,testue):
        
        spot = self.root
        new_node = Node(testue)

        if self.root == None:
            self.root = new_node
            return
        
        while True: #until according empty spot is found (spot.left or spot.right)
            if testue > spot.testue: #going right
                
                if spot.right == None:
                    spot.right = new_node
                    return

                else:
                    spot = spot.right

            elif testue < spot.testue: #going left

                if spot.left == None:
                    spot.left = new_node
                    return

                else:
                    spot = spot.left

            elif testue == spot.testue: #special case if testue inserted already exists
                return 

    def lookup(self,testue):
        
        spot = self.root
        
        while spot != None: #traverse tree according to rules
            if testue > spot.testue:
                spot = spot.right

            elif testue < spot.testue:
                spot = spot.left

            elif testue == spot.testue:
                return spot

        return print(testue, 'was not found')


    def traverse(self,node): #node should start with self.root when called
                             #prints all testues in the BST
                             #a pre-order DFS
        if node:
            print(node.testue)

        if node.left:
            self.traverse(node.left)
                
        if node.right:
            self.traverse(node.right)

        return

root = Node(9)
tree = BST(root)
tree.insert(4)
tree.insert(20)
tree.insert(1)
tree.insert(6)
tree.insert(15)
tree.insert(170)
tree.traverse(tree.root)
