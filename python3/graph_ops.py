#!/bin/python3

import os
import sys
from collections import defaultdict

class Graph:
    def __init__(self,e_list):
        self.graph = defaultdict(list)
        for edge in e_list:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])
        self.visited = []
        self.counts = defaultdict(int)
    def dfs_with_count(self,curr_v,starting_v):
        if curr_v not in self.visited:
            self.counts[starting_v]+=1
            self.visited.append(curr_v)
            for v in self.graph[curr_v]:
                self.dfs_with_count(v,starting_v)
def countElemConnectedComponentsInGraph(e_list):
    g = Graph(e_list)
    for v in g.graph.keys():
        tree=[]
        g.dfs_with_count(v,v)
    g.counts = [ c for c in g.counts.values() if c >1]
    
if __name__ == '__main__':
    gb = []
    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))

    result = countElemConnectedComponentsInGraph(gb)
