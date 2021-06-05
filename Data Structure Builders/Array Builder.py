Name: Terry Su
#Date: May 2, 2021
#Purpose: Building the some functions for an array from scratch using hash tables

class MyArray:
    
    def __init__ (self):
        self.length = 0
        self.data = {}

    def search(self,index):
        return print(self.data.get(index, 'index does not exist'))

    def append(self,item):
        self.data[self.length] = item
        self.length += 1

    def pop(self):
        self.data.pop(self.length-1)
        self.length -= 1

    def delete(self,index): 
        del self.data[index]
        self.shift(index)

    def shift(self,index):
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]
            
        del self.data[self.length-1] #length-1 bcuz index is always one less than length
        self.length -= 1

Test = MyArray()
Test.search(0)
Test.append(4)
Test.append(5)
Test.append(6)
Test.delete(1)
print(Test.data)
