#BIT Template (0-index based)

class BIT:

    def __init__(self,nums):
        self.nums = nums
        self.bit = [0]+nums
        for i in range(1,length:=len(self.bit)):
            if (j:=i+(i&-i)) < length:
                self.bit[j] += self.bit[i]
        return
        
    def update(self,index,val):
        i,diff = index+1,val-self.nums[index]
        self.nums[index] = val
        while i < len(self.bit):
            self.bit[i] += diff
            i += i&-i
        return

    def sum(self,left,right):
        def prefix_sum(i):
            res = 0
            while i>0:
                res += self.bit[i]
                i -= i&-i
            return res
        return prefix_sum(right+1) - prefix_sum(left)

x = BIT([1,2,3,4,5,6,7])
print(x.sum(1,2))
