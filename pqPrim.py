""" Prim's algorithm using minimalTemplate """
from newEdgy import *
import random
from queue import PriorityQueue

def generateGraph(n):
    """ Returns a graph object """
    G = nx.Graph()

    # Fill in graph nodes, edges and attributes
    G = nx.grid_graph([n, n])

    nx.set_edge_attributes(G, 'color', 'black')
    nx.set_edge_attributes(G, 'width', 0.5)
    for u, v in G.edges():
        G.edge[u][v]['weight'] = random.randint(5, 10)

    return G


def prim(G):
    """ Implementation of Prim's algorithm with a priority queue """

    toSearch = PriorityQueue()
    visited = list()

    u = random.choice(G.nodes())
    G.node[u]['color'] = 'green'
    visited.append(u)

    for neigh in G[u]:
        toSearch.put_nowait((G.edge[u][neigh]['weight'], (u, neigh)))

    while not toSearch.empty():
        priority, (v, w) = toSearch.get()
        if w in visited:
            continue
        G.edge[v][w]['color'] = 'red'
        G.edge[v][w]['width'] = 2
        G.node[w]['color'] = 'green'
        visited.append(w)
        for neigh in G[w]:
            if neigh not in visited:
                toSearch.put_nowait((G.edge[w][neigh]['weight'], (w, neigh)))
   
        yield True

    for u, v in G.edges():
        if G.edge[u][v]['color'] != 'red':
            G.edge[u][v]['color'] = 'lightgrey'
            
    yield False

def pruneTree(G):
    for u, v in G.edges():
        if G.edge[u][v]['color'] != 'red':
            G.remove_edge(u, v)
            
if __name__ == '__main__':
    G = generateGraph(3)
    
    animate(G, prim)
    pruneTree(G)
    pylab.cla()
    
    u = random.choice(G.nodes())
    show(G, setPos=hierarchy_pos(G, u), labelPos=0.5, edgeFontSize=12)
    
