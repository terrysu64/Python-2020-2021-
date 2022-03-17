#min/max range query sparse table template

import math
 
class MINsparse:
    
    def __init__(self,arr):
        n = len(arr)
        size = 500
        self.lookup = [[0 for i in range(size)] for j in range(size)]
        
        for i in range(0, n): self.lookup[i][0] = arr[i]
    
        j = 1
        while (1 << j) <= n:
            i = 0
            while (i + (1 << j) - 1) < n:
                if (self.lookup[i][j - 1] < self.lookup[i + (1 << (j - 1))][j - 1]): self.lookup[i][j] = self.lookup[i][j - 1]
                else: self.lookup[i][j] = self.lookup[i + (1 << (j - 1))][j - 1]
                i += 1
            j += 1

    def query(self,L,R):
        j = int(math.log2(R - L + 1))
        if self.lookup[L][j] <= self.lookup[R - (1 << j) + 1][j]:
            return self.lookup[L][j]
        else:
            return self.lookup[R - (1 << j) + 1][j]

class MAXsparse:
    
    def __init__(self,arr):
        n = len(arr)
        size = 500
        self.lookup = [[0 for i in range(size)] for j in range(size)]
        
        for i in range(0, n): self.lookup[i][0] = arr[i]
    
        j = 1
        while (1 << j) <= n:
            i = 0
            while (i + (1 << j) - 1) < n:
                if (self.lookup[i][j - 1] > self.lookup[i + (1 << (j - 1))][j - 1]): self.lookup[i][j] = self.lookup[i][j - 1]
                else: self.lookup[i][j] = self.lookup[i + (1 << (j - 1))][j - 1]
                i += 1
            j += 1

    def query(self,L,R):
        j = int(math.log2(R - L + 1))
        if self.lookup[L][j] >= self.lookup[R - (1 << j) + 1][j]:
            return self.lookup[L][j]
        else:
            return self.lookup[R - (1 << j) + 1][j]
            

