#Name: Terry Su
#Date: June 5, 2021
#Purpose: Building a binary search tree + some methods from scratch (not done)

class Node:

    #constructor for each node in the BST
    def __init__(self, value = None, left=None, right = None): #None is like null
        self.value = value
        self.left = left
        self.right = right

class BST: 

    def __init__(self,root = None):
        self.root = root

    def insert(self,value):
        
        spot = self.root.value
        
        while spot != None:
            if value > spot.value:
                
                if spot.right == None:
                    spot.right = value
                    return
                
                spot = spot.right

            elif value < spot.value:

                if spot.left == None:
                    spot.left = value
                    return
                
                spot = spot.left

            elif value == spot.value:
                return 

    def lookup(self,value):
        
        spot = self.root.value
        
        while spot != None:
            if value > spot.value:
                spot = spot.right

            elif value < spot.value:
                spot = spot.left

            elif value == spot.value:
                return spot

        return 'value not found'


    #def remove
