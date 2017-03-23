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

def algorithm(G):
    # Paramater must hold G

    yield True
    
    u = random.choice(G.nodes())

    G.node[u]['color'] = 'green'
    yield True

    G.node[u]['color'] = 'red'
    yield True

    # The last yield statement must be False
    yield False

if __name__ == '__main__':
    G = generateGraph()
    
    animate(G, algorithm)
    
