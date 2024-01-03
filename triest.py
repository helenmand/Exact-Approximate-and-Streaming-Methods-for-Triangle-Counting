import random
import networkx as nx 
import tools

def triest_base(G, M):
    sample = nx.empty_graph()
    t = 0
    global_estimate = 0

    for edge in G.edges(): 
        t+=1

        if tools.sample_edge(sample=sample,
                      u=edge[0], v=edge[1],
                       M=M, t=t):
            sample.add_edge(edge[0], edge[1])
            global_estimate = tools.update_counters_base(sample=sample,
                                                   u=edge[0], v=edge[1],
                                                   global_est=global_estimate)

    return global_estimate

def triest_impr(G, M):
    sample = nx.empty_graph()
    t = 0
    global_estimate = 0

    for edge in G.edges():
       t += 1
       global_estimate = tools.update_counters_impr(sample=sample,
                                              u=edge[0], v=edge[1],
                                              M=M, t=t,
                                              global_est=global_estimate)
       if tools.sample_edge(sample=sample,
                      u=edge[0], v=edge[1],
                      M=M, t=t):
          sample.add_edge(edge[0], edge[1])
        
    return global_estimate