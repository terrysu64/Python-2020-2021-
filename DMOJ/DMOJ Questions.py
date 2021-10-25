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

#Date: October 24, 2021
#https://dmoj.ca/problem/ccc10j5

#O(2^n) bfs with memoization optimization
#row and col 1-8 cartesian

op,ed = [int(x) for x in input().split()], [int(x) for x in input().split()]
seen = set()
mvs = [[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1],[-1,2]]
spts = [op]

ans = 0
while spts:
    temp = []
    found = False
    for sp in spts:
        if sp==ed:
            found = True
            break
        seen.add(tuple(sp))
        for m in mvs:
            pos=[sp[0]+m[0],sp[1]+m[1]]
            if 1<=pos[0]<=8 and 1<=pos[1]<=8 and tuple(pos) not in seen:
                temp += [pos]
    if found: break
    spts = temp
    ans += 1

print(ans)

#Date: October 24, 2021
#https://dmoj.ca/problem/ccc14s2

#an O(n) set/hashmap solution
#couldnt use walrus operator because DMOJ pypy3 is based on python 3.7.3

n = int(input())
given = list(zip(input().split(),input().split()))
pts = {}

for g in given:
    if (g[1],g[0]) in pts:
        pts.pop((g[1],g[0]))
        continue
    pts[g] = True

if pts: print('bad')
else: print('good')
    