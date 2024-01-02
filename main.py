import networkx as nx
import numpy as np
import exact as e
import doulion as d
import triest as t

"""
# dataset : n_triangles
# zachary : 45 
# example : 5 
# roadpa : 67150 - med
# astroph : 1351441 - big
# email : 105461 - small
"""

g = nx.read_edgelist(f"data/astroph.txt",create_using=nx.Graph(), nodetype = int)
g.remove_edges_from(nx.selfloop_edges(g)) # removing self-loops (if any)

#print(e.all_triplets(G=g))
print(f"NodeIterator Results: {e.node_iter(G=g)}")

print(f"Doulion with NodeIterator Results: {d.DOULION_NodeIterator(G=g, p=0.69)}")

print(f"Triest base result: {t.triest_base(G=g, M=14000)}")
print(f"Triest improved result: {t.triest_impr(G=g, M=14000)}")  
       