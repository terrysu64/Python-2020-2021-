#Date: October 21, 2021
#Author: Terry Su
#Purpose: My own implementation of Dijkstra's Shortest Path Algorithm from scratch

import heapq

#Time complexity: O(v^2 + vlogv)
#Space complexity: O(v)
#where v is the number of vertices in the graph

def solve(adj,stt): #solve for shortest path from a starting node based on adjacency matrix of a weighted graph

    if not adj or len(adj)==1: return 0
    unvis = {i for i in range(len(adj))}
    tab = {i:float('inf') for i in range(len(adj))}
    tab[stt] = 0

    while unvis:
        curr = sorted(unvis,key=lambda x:tab[x])[0]
        for i in range(len(adj[curr])):
            if i in unvis and adj[curr][i]: tab[i] = min(tab[i],tab[curr]+adj[curr][i])
        unvis.remove(curr)
        print(curr, tab[curr]) #destination, shortest path
    

#Nodes are A,B,C,D,E (indices 0,1...)
test1 = [[0,6,None,1,None],
         [6,0,5,2,2],
         [None,5,0,None,5],
         [1,2,None,0,1],
         [None,2,5,1,0]]

test2 = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]

#solve(test1,0)
#solve(test1,1)
#solve(test2,0)
