#top sort template

from collections import defaultdict,deque
        
adj,unvis=defaultdict(list),{i for i in range(numCourses)}
for p in prereq: adj[p[1]] += [p[0]]

def dfs(node,pars):
    nonlocal unvis,cyc
    if node in adj:
        for pos in adj[node]:
            if pos in pars: cyc=True; return #cycle found
            if pos in unvis: unvis.remove(pos); dfs(pos,pars|{pos})
    ans.appendleft(node)
    
ans = deque()
while unvis:
    cyc,curr=False,unvis.pop()
    dfs(curr,{curr})
    if cyc: return []
