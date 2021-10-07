#Date: October 7, 2021
#https://dmoj.ca/problem/a3

N = int(input())
for t in range(N):
    curr = int(input())+1
    while True:
        if str(curr**3)[-1:-4:-1] == '888':
            print(curr)
            break
        curr += 1

#Date: October 7, 2021:
#https://dmoj.ca/problem/aac1p4/submit

#TLE ON BATCH 3 O(n)

def solve(arr):
    l,r,targ = [int(n) for n in input().split()]
    l -= 1
    r -= 1
    seen = set()
    for i in range(l,r+1):
        if all([targ/arr[i]==(div:=targ//arr[i]), div!=arr[i], div in seen]):
            return 'YES'
        seen.add(arr[i])
    return 'NO'

q = int(input().split()[1])
arr = [int(x) for x in input().split()]
for _ in range(q):
    print(solve(arr))
