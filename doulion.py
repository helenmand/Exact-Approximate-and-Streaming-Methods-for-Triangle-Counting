# implementation of approximate algorithm DOULION
import networkx as nx
import numpy as np
import exact as e

np.random.seed(42)

def spasify_graph(G, p):
    sparse_graph = nx.Graph() # empty graph

    for x, y in G.edges():
        # if probability p is greater that a random number
        if np.random.random() <= p: 
            sparse_graph.add_edge(x, y) # add the edge

    return sparse_graph 

def DOULION_NodeIterator(G, p):
    graph = spasify_graph(G, p=p)
    num_of_triangles = e.node_iter(G=graph) 

    return format(num_of_triangles/p**3, ".0f")

def DOULION_compact_forward(G, p):
    graph = spasify_graph(G, p=p)
    num_of_triangles = e.compact_forward(G=graph) 

    return format(num_of_triangles/p**3, ".0f")


