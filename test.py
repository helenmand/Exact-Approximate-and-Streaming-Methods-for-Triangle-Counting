import time
import numpy as np

def c_forward(graph):
    '''runs Compact Forward algorithm & returns the total number of triangles in the network''' 
    
    time_start_cf = time.process_time()   
    tri = 0 
    vertices = graph.nodes()
    degrees = [graph.degree(v) for v in vertices]
    # Sort nodes based on decreasing order of degree
    newDeg, newVer = zip(*sorted(zip(degrees, vertices), reverse=True))
    newDeg, newVer = np.array(newDeg), np.array(newVer)
    ver_dict = dict(zip(newVer, range(len(newVer))))  # dict node_id:index
    i = 0
    for v in newVer:
        neighbors = list(graph.neighbors(v))
        if len(neighbors) > 0:
            # Sort neighbors also in decreasing order of degree
            nei_degrees = [graph.degree(u) for u in neighbors]
            newNeiDeg, newNeiVer = zip(*sorted(zip(nei_degrees, neighbors), reverse=True))
            idx_base = i
            # If the smallest degree is higher than v's degree, ignore
            idx_check = ver_dict[newNeiVer[-1]]
            if idx_check > idx_base:
                neib = filter(lambda item: ver_dict[item] > idx_base, newNeiVer)

                for u in neib:  # keep only neighbors with lower degree                           
                    u_neighbors = list(graph.neighbors(u))
                    u_nei_degrees = [graph.degree(i) for i in u_neighbors]
                    _, newNei_u = zip(*sorted(zip(u_nei_degrees, u_neighbors), reverse=True))
                    u1 = newNei_u[0]  # first neighbor of u
                    v1 = newNeiVer[0]  # first neighbor of v
                    c_u = 0  # counter for neighbors of u
                    c_v = 0  # counter for neighbors of v
                    idx_candid1 = ver_dict[u1]
                    idx_candid2 = ver_dict[v1]                
                   
                    while c_u < len(newNei_u) and c_v < len(newNeiVer):
                        if idx_candid1 > idx_base and idx_candid2 > idx_base:
                            if u1 == v1:
                                tri += 1
                            if idx_candid1 < idx_candid2:
                                c_u += 1
                                if c_u < len(newNei_u):
                                    u1 = newNei_u[c_u]
                                    idx_candid1 = ver_dict[u1]
                            else:
                                c_v += 1
                                if c_v < len(newNeiVer):
                                    v1 = newNeiVer[c_v]
                                    idx_candid2 = ver_dict[v1]
                        elif idx_candid1 <= idx_base:
                            c_u += 1
                            if c_u < len(newNei_u):
                                u1 = newNei_u[c_u]
                                idx_candid1 = ver_dict[u1]
                        elif idx_candid2 <= idx_base:
                            c_v += 1
                            if c_v < len(newNeiVer):
                                v1 = newNeiVer[c_v]
                                idx_candid2 = ver_dict[v1]
        i += 1
    time_of_cf = (time.process_time() - time_start_cf)         
    return tri//3, time_of_cf
