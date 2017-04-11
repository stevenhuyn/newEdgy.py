"""Minimal Template
More Concise, less junk to look at
More focus on the program
"""
from newEdgy import *
import random

def generateGraph():
    """ Returns a graph object """
    G = nx.Graph()

    # Fill in graph nodes, edges and attributes
    G = nx.grid_graph([3, 3])

    return G

def algorithm(G, u):
    # Paramater must hold G

    # Yield true every time G is to be drawn
    yield True

    G.node[u]['color'] = 'green'
    yield True

    G.node[u]['color'] = 'red'
    yield True

    dfs = nx.dfs_edges(G, source=u)
    for v, w in dfs:
        nx.dfs_edges
        G.add_edge(v, w, width=3, color='red')
        yield True

    # The last yield statement must be False
    yield False

def main():
    G = generateGraph()
    initialNode = random.choice(G.nodes())
    animate(G, algorithm, u=initialNode)

if __name__ == '__main__':
    main()

    
    
