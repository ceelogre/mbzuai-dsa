class Node:
  def __init__(self, data):
    self.data = data
    self.neighbors = []
  
  def add_neighbor(self, new_node):
    self.neighbors.append(new_node)
  
  def __repr__(self):
    return self.data


class Graph:
  def __init__(self):
    self.nodes = []
  
  def add_node(self, node):
    self.nodes.append(node)
  
  def add_edge(self, node_1, node_2):
    node_1.add_neighbor(node_2)
    node_2.add_neighbor(node_1)
  
  def dfs_visit(self, start, visited=None):
    if visited is None:
      visited = set()
    visited.add(start)
    for node in start.neighbors:
      if node not in visited:
        self.dfs_visit(node, visited)

    return visited

  def find_all_paths(self, start, end, path=[]):
    path = path + [start]
    if start == end:
      return [path]
    
    paths = []
    for node in start.neighbors:
      if node not in path:
        newpaths = self.find_all_paths(node, end, path)

        #add new paths to the existing paths
        for newpath in newpaths:
          paths.append(newpath)
    return paths

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

print(my_graph.dfs_visit(B))

all_paths = (my_graph.find_all_paths(A,B))

#find the shortest path
