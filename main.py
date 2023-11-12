import networkx as nx
import exact as e

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
# zachary : 45 YYY
# example : 5 YYY
# roadpa : 67150 YYN
# astroph : 1351441 YNN
# email : 105461 YNN
"""

g = nx.read_edgelist(f"data/email.txt",create_using=nx.Graph(), nodetype = int)

# zachary missing 6 7 17 triangle
#print(e.all_triplets(G=g))
print(e.node_iter(G=g))
#print(e.compact_forward_gpt(G=g))
print(e.compact_forward(G=g))

