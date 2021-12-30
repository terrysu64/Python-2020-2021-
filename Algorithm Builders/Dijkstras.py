#Date: October 21, 2021
#Author: Terry Su
#Purpose: My own implementation of Dijkstra's Shortest Path Algorithm from scratch


#Time complexity: O(v + vlogv) with priority queue template
#Space complexity: O(v)
#where v is the number of vertices in the graph

import collections
import heapq
import itertools

#lower value = higher priority

class PriorityQueue(collections.UserDict):
    def __init__(self):
        super().__init__(self)
        self.heap = []
        self.counter = itertools.count()

    def pq_add(self, task, priority):
        if task in self: self.pq_remove(task)
        record = [priority, next(self.counter), task]
        self[task] = record
        heapq.heappush(self.heap, record)

    def pq_remove(self, task):
        if task in self:
            record = self.pop(task)
            record[-1] = None

    def pq_pop(self):
        while self.heap:
            priority, _, task = heapq.heappop(self.heap)
            if task != None:
                del self[task]
                return [task,priority]
        else:
            raise RuntimeError('Heap is empty.')

    def info(self,task):
        if task not in self: return False
        return self[task]

def solve(adj,stt): #solve for shortest path from a starting node based on adjacency matrix of a weighted graph

    if not adj or len(adj)==1: return 0
    unvis = {i for i in range(len(adj))}
    pq = PriorityQueue()
    for i in range(len(adj)): pq.pq_add(i,float('inf'))
    pq.pq_add(stt,0)
    
    while unvis:
        curr,dis = pq.pq_pop()
        for i in range(len(adj[curr])):
            if i in unvis and adj[curr][i] and pq.info(i)[0] > dis+adj[curr][i]: pq.pq_add(i,dis+adj[curr][i])
        unvis.remove(curr)
        print(curr,dis) #destination, shortest path
    

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

solve(test1,0)
#solve(test1,1)
solve(test2,0)
