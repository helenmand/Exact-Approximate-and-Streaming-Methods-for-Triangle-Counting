import networkx as nx
import random

def coin_flip(head_prob):
    coin_toss = random.random()
    
    return coin_toss < head_prob

def spasify_graph(G, p):
    sparse_graph = nx.Graph() # empty graph

    for x, y in G.edges():
        if coin_flip(p): 
            sparse_graph.add_edge(x, y) # add the edge

    return sparse_graph 

def flip_biased_coin(M,t):
  head_prob = random.random()
  
  if head_prob <= M/t:
      return True
  else:
      return False

def sample_edge(sample, M, t):
  if t <= M:
    return True
  elif flip_biased_coin(M,t):
    random_edge = random.choice(list(sample.edges))
    sample.remove_edge(*random_edge)
    return True
  
  return False

def sample_edge_base(sample, M, t, u, v, global_est):
  if t <= M:
    return True, global_est
  elif flip_biased_coin(M,t):
    random_edge = random.choice(list(sample.edges))
    sample.remove_edge(*random_edge)
    global_est = update_counters_base(sample, u, v, global_est, -1)
    return True, global_est
  
  return False, global_est

def update_counters_base(sample, u, v, global_est, val):
  if (u in sample.nodes) & (v in sample.nodes):
    common_neighbors = list(sorted(nx.common_neighbors(sample, u, v)))
    
    if not common_neighbors:
      return global_est

    for _ in common_neighbors:
      global_est += val
  
  return global_est 

def update_counters_impr(sample, u, v, M, t, global_est):
  if (u in sample.nodes) & (v in sample.nodes):
    common_neighbors = list(sorted(nx.common_neighbors(sample, u, v)))
    
    if not common_neighbors:
      return global_est
    
    h = max(1, int(((t-1)*(t-2))/(M * (M - 1))))
    
    for _ in common_neighbors:
      global_est += h
  
  return global_est 