#Name: Terry Su
#Date: May 9, 2021
#Purpose: Building a SINGLY linked list + some methods from scratch

#ideal linked list
#head --> node --> node -->... --> tail
MyLinkedList = {
    'head': {
        'value': 10,
        'next_node': {
            'value': 5,
            'next_node': {
                'value': 16,
                'next_node' : 'done'}}}} #done = null in this case
 
print(MyLinkedList['head']['next_node']['next_node']['value'], '\n') #3 values into the linked list
    
#A single node of a singly linked list
class Node:

    #constructor (each node is an object in this class)
    def __init__(self, data = None, next=None): #None is like null
        self.data = data
        self.next = next


#A Linked List class with a single head node
class LinkedList:
    def __init__(self):
        self.head = None #initial head node
  
    def append(self, data):
        newNode = Node(data)
    
        if(self.head): #if head node exists
            current = self.head

            while(current.next): #allows us to reach none/null
              current = current.next
            current.next = newNode

        else:
            self.head = newNode

    def pop(self):
        
        current = self.head

        if current.next == None: #in case the head is the only node in the linked list
            self.head = None
            return
        
        while(current.next.next):
            current = current.next
        current.next = None
            
    def printLL(self):
        
        current = self.head
        
        while(current):
            print(current.data)
            current = current.next

    def lookup(self,index):
        
        counter = 0
        current = self.head
        
        while counter != index: #traverse through the list until index is reached
            current = current.next
            counter += 1

        return current.data
    
    def lookup2(self,index):
        
        counter = 0
        current = self.head
            
        while counter != index: #traverse through the list until index is reached
            current = current.next
            counter += 1

        return current

    def insert(self,index,value): #assuming valid index that <= max existing index

        #diagram:
        # * - *  =>  *    * (on hold)  => *    * => *-*-*
        #   *         \                    \  /
        #               *                    *

        new_node = Node(value)
        
        leader = self.lookup2(index-1) #need to specify self in params bcuz its a nested function
        hold = leader.next
        leader.next = new_node
        new_node.next = hold

    def remove(self,index):
        leader = self.lookup2(index-1)
        leader.next = leader.next.next
        

# Singly Linked List with insertion and print methods
Test = LinkedList()
Test.append(3)
Test.append(5)
Test.append(6)


    

