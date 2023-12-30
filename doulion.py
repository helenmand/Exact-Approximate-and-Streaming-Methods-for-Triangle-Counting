# implementation of approximate algorithm DOULION
import networkx as nx
import numpy as np
import exact as e
import tools as tools

np.random.seed(42)

def DOULION_NodeIterator(G, p):
    graph = tools.spasify_graph(G, p=p)
    num_of_triangles = e.node_iter(G=graph) 

    return format(num_of_triangles/p**3, ".0f")

def DOULION_compact_forward(G, p):
    graph = tools.spasify_graph(G, p=p)
    num_of_triangles = e.compact_forward(G=graph) 

    return format(num_of_triangles/p**3, ".0f")
