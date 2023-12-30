import networkx as nx
import numpy as np
import exact as e
import doulion as d

"""
file_num = int(input(print("Choose your desired dataset:\n1 for facebook\t2 for email\n3 for zachary\t4 for example")))

if file_num == 1:
    file_name = "facebook"
elif file_num == 2:
    file_name = "email"
elif file_num == 3:
    file_name = "zachary"
else:
    file_name = "example

g = nx.read_edgelist(f"data/{file_name}.txt",create_using=nx.Graph(), nodetype = int)
"""

"""
# dataset : n_triangles
# zachary : 45 YYN
# example : 5 YYY
# roadpa : 67150 YYN
# astroph : 1351441 YYN
# email : 105461 YYN
"""

g = nx.read_edgelist(f"data/roadpa.txt",create_using=nx.Graph(), nodetype = int)
g.remove_edges_from(nx.selfloop_edges(g)) # removing self-loops (if any)

# zachary missing 6 7 17 triangle
print(e.all_triplets(G=g))
print(e.node_iter(G=g))
print(e.compact_forward(G=g))

print(d.DOULION_compact_forward(G=g, p=0.7))
print(d.DOULION_NodeIterator(G=g, p=0.7))
