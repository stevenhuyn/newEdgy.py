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

def main():
    G = generateGraph()
    show(G)

if __name__ == '__main__':
    main()

    
    
