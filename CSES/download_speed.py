# MAX FLOW
# Edmonds Karp, shortest augmenting path
from dataclasses import dataclass
from collections import deque

n, m = map(int, input().split())

@dataclass
class EdgeInfo:
  frm: int
  to: int
  id: int
  forward: bool

class FlowGraph:
  def __init__(self, number_of_nodes):
    self.adjacency:list = [[] for _ in range(number_of_nodes)]
    self.flow = []
    self.capacity = []
  
  def add_edge(self, frm, to, capacity):
    self.adjacency_list[frm].append(EdgeInfo(frm, to, len(self.flow), True))
    self.adjacency_list[to].append(EdgeInfo(to, frm, len(self.flow), False))
    self.flow.append(0)
    self.capacity.append(capacity)
  
  def add_flow(self, edgeInfo, flow):
    if edgeInfo.forward:
      self.flow[edgeInfo.id] += flow
    else:
      self.flow[edgeInfo.id] -= flow
  
  def traversable(self, edge):
    return self.left_over_capacity(edge) > 0
  
  def left_over_capacity(self, edgeInfo):
    if edgeInfo.forward:
      return self.capacity[edgeInfo.id] - self.flow[edgeInfo.id]
    else:
      return self.flow[edgeInfo.id]

def bfs(graph, n, source, dest):
  edge_taken = [None for _ in range(n)]
  visited = [False for _ in range(n)]
  visited[source] = True
  queue = deque()
  queue.append(source)
  
  while queue:
    v = queue.popleft()
    for edge in graph.adjacency_list[v]:
      if graph.traversable(edge) and not visited[edge.to]:
        visited[edge.to] = True
        edge_taken[edge.to] = edge
        queue.append(edge.to)
        
  if visited[dest]:
    edges_used = []
    node = dest
    while edge_taken[node]:
      edges_used.append(edge_taken[node])
      node = edge_taken[node].frm
    
    return edges_used
  
  return None

def edmond_karp(graph, n, source, dest):
  while True:
    path = bfs(graph, n, source, dest)
    if path is None:
      break
    
    flow = graph.left_over_capaciity(path[0])
    for edge in path:
      flow = min(flow, graph.left_over_capacity(edge))
    
    for edge in path:
      graph.add_flow(edge, flow)
      
  total_flow = 0
  for edge in graph.adjacency_list[source]:
    if edge.forward:
      total_flow += graph.flow[edge.id]
  
  return total_flow

graph = FlowGraph(n)

for _ in range(n):
  v, u, c = map(int, input().split())
  v -= 1
  c -= 1
  
  graph.add_edge(v, u, c)
  
flow = edmond_karp(graph, n, 0, n-1)

print(flow)