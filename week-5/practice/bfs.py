class Node:
  def __init__(self, data):
    self.data = data
    self.neighbors = []

  def add_neighbors(self, node):
    self.neighbors.append(node)

  def __repr__(self):
    return self.data


class Graph:
  def __init__(self):
    self.nodes = []
  
  def add_node(self, node):
    self.nodes.append(node)
  
  def add_edge(self, node_1, node_2):
    node_1.add_neighbors(node_2)
    node_2.add_neighbors(node_1)
  

  def bfs_visit(self, start, visited=None):
    if visited is None:
      discovered = set()
    discovered.add(start)
    queue = [start]
    while queue:
      current_node = queue.pop(0)
      for node in current_node.neighbors:
        if node not in discovered:
          discovered.add(node)
          queue.append(node)
      
    return discovered
  
  def bfs_visit_(self, start, visited=None):
    #re-write the above function using recursion
    pass

  def find_shortest_path(self, start, end, path=[]):
    path = path + [start]
    if start == end:
      return path

    shortest_path = None
    for node in start.neighbors:
      if node not in path:
        new_path = self.find_shortest_path(node, end, path)
        if new_path:
          if not shortest_path or len(new_path) < len(shortest_path):
            shortest_path = new_path
    return shortest_path

B = Node('B')
A = Node('A')
#initialize an empty graph
my_graph = Graph()

#add nodes to the graph
my_graph.add_node(A)
my_graph.add_node(B)
my_graph.add_edge(A, B)

#add more nodes
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
my_graph.add_node(C)
my_graph.add_node(D)
my_graph.add_node(E)
my_graph.add_node(F)

my_graph.add_edge(A,C)
my_graph.add_edge(A,D)
my_graph.add_edge(C, E)
my_graph.add_edge(B, E)
my_graph.add_edge(D, E)
my_graph.add_edge(B, F)
my_graph.add_edge(E,F)

print(my_graph.bfs_visit(A))
print(my_graph.find_shortest_path(A, F))