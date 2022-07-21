class seg:
    def __init__(self,arr):
        N = 100000
        self.n = len(arr)
        self.tree = [0] * (2 * N)        
        for i in range(self.n) :
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1) :
            self.tree[i] = max(self.tree[i << 1],self.tree[i << 1 | 1])
     
    def update(self,idx, val) :
        self.tree[idx + self.n] = val
        idx += self.n
        i = idx;
        while i > 1:
            self.tree[i >> 1] = max(self.tree[i],self.tree[i ^ 1])
            i >>= 1
     
    def query(self,l, r):
        r += 1
        res = 0
        l += self.n
        r += self.n
        while l < r:
            if (l & 1):
                res = max(res,self.tree[l])
                l += 1
            if (r & 1) :
                r -= 1
                res = max(res,self.tree[r])
            l >>= 1
            r >>= 1
        return res

test = seg([3, 2, 1, 2, 1])

