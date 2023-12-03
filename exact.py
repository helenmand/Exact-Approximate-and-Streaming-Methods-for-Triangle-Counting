from itertools import combinations
import time
import networkx as nx
import numpy as np

# exact algorithms to find triangles in a graph
# all triplets
def all_triplets(G):
    num_of_triangles = 0

    for triplet in combinations(G.nodes, 3):
        x, y, z = sorted(triplet)

        if G.has_edge(x, y) and G.has_edge(y, z) and G.has_edge(x, z):
            num_of_triangles += 1
    return num_of_triangles

# node iterator
def node_iter(G):
    num_of_triangles = 0

    for node in G.nodes:
        neighbors = list(G.neighbors(node))
        
        if len(neighbors) > 1:
            neighbors_combinations = combinations(neighbors, 2)
            
            for x, y in neighbors_combinations:
                if G.has_edge(x, y) or G.has_edge(y, x):
                    num_of_triangles += 1

    return num_of_triangles//3

# compact forward
def compact_forward_gpt(G):
    # simplified by chatgpt 
    num_of_triangles = 0
    
    nodes = G.nodes()
    degrees = np.array([G.degree(node) for node in nodes])

    sorted_nodes = np.array(nodes)[np.argsort(degrees)[::-1]]

    for node in sorted_nodes:
        neighbors = list(G.neighbors(node))
        neighbors_degrees = np.array([G.degree(n) for n in neighbors])

        sorted_neighbors = np.array(neighbors)[np.argsort(neighbors_degrees)[::-1]]

        for i in range(len(sorted_neighbors)):
            u = sorted_neighbors[i]
            for j in range(i + 1, len(sorted_neighbors)):
                v = sorted_neighbors[j]

                if G.has_edge(u, v):
                    num_of_triangles += 1

    return num_of_triangles // 3

def compact_forward(G):
    num_of_triangles = 0
    # 1
    nodes = G.nodes()
    degrees = np.array([G.degree(node) for node in nodes])

    sorted_nodes = np.array(nodes)[np.argsort(degrees)[::-1]]
    node_dict = dict(zip(sorted_nodes, range(len(sorted_nodes)))) # node_id : index

    for node in sorted_nodes: # 3
        # 2
        neighbors = list(G.neighbors(node))
        neighbors_degrees = np.array([G.degree(n) for n in neighbors])

        sorted_neighbors = np.array(neighbors)[np.argsort(neighbors_degrees)[::-1]]
    
        for neighbor in sorted_neighbors:
            if node_dict[node] < node_dict[neighbor]: # 3a
                # neighbors of the neighbor 
                # 2
                n_neighbors = list(G.neighbors(neighbor))
                n_neighbors_degrees = np.array([G.degree(n) for n in n_neighbors])

                sorted_n_neighbors = np.array(n_neighbors)[np.argsort(n_neighbors_degrees)[::-1]]
                
                n = iter(sorted_neighbors)
                nn = iter(sorted_n_neighbors)

                # 3aa
                v_ = next(n)
                u_ = next(nn)

                while n.__length_hint__() > 0 and nn.__length_hint__() > 0 \
                      and node_dict[u_] < node_dict[node] and \
                          node_dict[v_] < node_dict[node] : # 3ab
    
                    if node_dict[u_] < node_dict[v_]: # 3aba
                        u_ = next(nn)
                    elif node_dict[u_] > node_dict[v_]: # 3abb
                        v_ = next(n)
                    else: # 3abc
                        num_of_triangles += 1 # 3abca
                        v_ = next(n) # 3abcb
                        u_ = next(nn) # 3abcc

    return num_of_triangles