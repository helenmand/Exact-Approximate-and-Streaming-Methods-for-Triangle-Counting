import networkx as nx
import numpy as np
import exact as e
import doulion as d
import triest as t

"""
# dataset : n_triangles
# zachary : 45 
# example : 5 
# roadpa : 67150 - big
# astroph : 1351441 - med
# email : 105461 - small
"""

g = nx.read_edgelist(f"data/email.txt",create_using=nx.Graph(), nodetype = int)
g.remove_edges_from(nx.selfloop_edges(g)) # removing self-loops (if any)

#print(e.all_triplets(G=g))
print(f"NodeIterator Results: {e.node_iter(G=g)}")

print(f"Doulion with NodeIterator Results: {d.DOULION_NodeIterator(G=g, p=0.69)}")

print(f"Triest base result: {t.triest_base(G=g, M=15000)}")
print(f"Triest improved result: {t.triest_impr(G=g, M=15000)}")  

# Results to point:
# astroph.txt
# M = 12500
# Triest base result: 17288
# Triest improved result: 1349087