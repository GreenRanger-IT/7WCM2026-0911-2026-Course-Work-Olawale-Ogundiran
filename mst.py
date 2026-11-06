# Ask: Code and create a MST using either Prim's or Kruskal MST algorithm for 3 different connected graphs

# Steps
# 1. create a connected Graph, undirected and weighted graph A with 6 nodes and 11 edges.
# 2. create mst function, elect for Prim's Algorithm
# 3. call mst function for Graph A (connect, undirected, weighted)
# 4. Depict final MST 
# 5. Repeat step 1-4 from B and C with V=5, E=8 

import matplotlib.pyplot as mp
import networkx as nx

# 1. create Graphs with arbitrary weights because it's an MST problem
# a defined as G(V,E), V={a,b,c,d,e,f}, E={(a,b,1),(a,c,1),(a,e,2),(a,f,3),(b,d,2),(b,e,4),(b,f,1),(c,d,3),(c,e,6),(d,f,4),(e,f,5)}
# b defined as G(V,E), V={a,b,c,d,e}, E={(a,b,2),(a,c,1),(a,d,2),(a,e,3),(b,c,4),(b,d,2),(b,e,5),(c,d,3)}
# c defined as G(V,E), V={a,b,c,d,e}, E={(a,b,3),(a,c,2),(a,e,1),(b,d,2),(b,e,1),(c,d,4),(c,e,2),(d,e,1)}

# build and depict graphs a,b,c
# build reusable graph building function

def create_graph(nodes,weighted_edges):
  G = nx.Graph()
  G.add_nodes_from(nodes)
  edges = [(u,v,{'weight': w}) for u,v,w in weighted_edges]
  G.add_edges_from(edges)
  return G


nodes_a=["a","b","c","d","e","f"]
edges_a=[("a","b",1),("a","c",1),("a","e",2),("a","f",3),("b","d",3),("b","e",4),("b","f",1),("c","d",3),("c","e",6),("d","f",4),("e","f",5)]

nodes_b=["a","b","c","d","e"]
edges_b=[("a","b",2),("a","c",1),("a","d",2),("a","e",3),("b","c",4),("b","d",2),("b","e",5),("c","d",3)]

nodes_c=["a","b","c","d","e"]
edges_c=[("a","b",3),("a","c",2),("a","e",1),("b","d",2),("b","e",1),("c","d",4),("c","e",2),("d","e",1)]

graph_a= create_graph(nodes_a,edges_a)
graph_b= create_graph(nodes_b,edges_b)
graph_c= create_graph(nodes_c,edges_c)

# graph layout
# pos_a=nx.circular_layout(graph_a)
# nx.draw_networkx_nodes(graph_a,pos_a)
# nx.draw_networkx_edges(graph_a,pos_a)
# edge_labels = nx.get_edge_attributes(graph_a,'weight')
# nx.draw_networkx_edge_labels(graph_a,pos_a, edge_labels)

# pos_b=nx.circular_layout(graph_b)
# nx.draw_networkx_nodes(graph_b,pos_b)
# nx.draw_networkx_edges(graph_b,pos_b)
# edge_labels = nx.get_edge_attributes(graph_b,'weight')
# nx.draw_networkx_edge_labels(graph_b,pos_b, edge_labels)

pos_c=nx.circular_layout(graph_c)
nx.draw_networkx_nodes(graph_c,pos_c)
nx.draw_networkx_edges(graph_c,pos_c)
edge_labels = nx.get_edge_attributes(graph_c,'weight')
nx.draw_networkx_edge_labels(graph_c,pos_c, edge_labels)

mp.show()


# create Prim's mst function
# Prim's algorithm starts from a vertex and expands to unvisited vertex while selecting the cheapest (minimum weight) edge.

#def MyMinimumSpanningTree(Graph) -> Graph:
  # initializa an empty graph
  #mst = nx.Graph()

  # pick starting node
  #starting_node = list(Graph.nodes())[0]

# couldn't quite work out how to code prim or kruskal.
  