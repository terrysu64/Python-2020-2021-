from math import ceil,log2
class lazyseg:
    def __init__(self,arr):
        self.n = len(arr); need = 2**(ceil(log2(self.n))+1)
        self.arr = arr
        self.tree = [0 for _ in range(need)]
        self.lazy = [0 for _ in range(need)]
        self.init(0,self.n-1,0)

    def init(self,l,r,i):
        if l>r: return
        if l==r: self.tree[i]=self.arr[l]; return
        m=(l+r)//2
        self.init(l,m,i*2+1)
        self.init(m+1,r,i*2+2)
        self.tree[i] = max(self.tree[i*2+1],self.tree[i*2+2])

    def updateRange(self,i,l,r,op,ed,add):
        if self.lazy[i]:
            self.tree[i] += self.lazy[i]
            if l!=r:
                self.lazy[i*2+1] += self.lazy[i]
                self.lazy[i*2+2] += self.lazy[i]
            self.lazy[i]=0
        if any([l>r,l>ed,r<op]): return
        if l>=op and r<=ed:
            self.tree[i] += add
            if l!=r:
                self.lazy[i*2+1]+=add
                self.lazy[i*2+2]+=add
            return
        m=(l+r)//2
        self.updateRange(i*2+1,l,m,op,ed,add)
        self.updateRange(i*2+2,m+1,r,op,ed,add)
        self.tree[i] = max(self.tree[i*2+1],self.tree[i*2+2])
    
    def update(self,op,ed,add):
        self.updateRange(0,0,self.n-1,op,ed,add)

    def queryRange(self,i,l,r,op,ed):
        if self.lazy[i]:
            self.tree[i] += self.lazy[i]
            if l!=r:
                self.lazy[i*2+1] += self.lazy[i]
                self.lazy[i*2+2] += self.lazy[i]
            self.lazy[i]=0
        if any([l>r,l>ed,r<op]): return 0
        if l>=op and r<=ed: return self.tree[i]
        m=(l+r)//2
        resl = self.queryRange(2*i+1,l,m,op,ed)
        resr = self.queryRange(2*i+2,m+1,r,op,ed)
        return max(resl,resr)

    def query(self,op,ed):
        return self.queryRange(0,0,self.n-1,op,ed)






