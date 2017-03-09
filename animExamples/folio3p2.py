"""
Visualising the MHS PBX system
"""
from edgy import *
import random

def generate():
    nodeList = list(range(31))
    edgeList = ( (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8),
                 (0, 9), (1, 10), (2, 11), (2, 12), (2, 13), (2, 14), (3, 15),
                 (3, 16), (3, 17), (3, 18), (4, 19), (4, 20), (5, 21), (6, 22),
                 (6, 23), (7, 24), (7, 25), (7, 26), (8, 27), (8, 28), (9, 29),
                 (9, 30))
    
    G = nx.Graph()
    G.add_nodes_from(nodeList)
    G.add_edges_from(edgeList)

    return G

def sim1(G, u, v):
    # Question 1
    nx.set_edge_attributes(G, 'color', 'grey')
    nx.set_edge_attributes(G, 'width', 0.5)
    yield True
    G.node[u]['color'] = 'green'
    yield True

    firstPhone = G.neighbors(u)[0]
    G.node[firstPhone]['color'] = 'yellow'
    G.edge[u][firstPhone]['color'] = 'red'
    G.edge[u][firstPhone]['width'] = 2
    yield True

    G.node[0]['color'] = 'yellow'
    G.edge[0][firstPhone]['color'] = 'red'
    G.edge[0][firstPhone]['width'] = 2
    yield True

    for phone in G.neighbors(0):
        if v in G.neighbors(phone):
            G.node[phone]['color'] = 'yellow'
            G.edge[0][phone]['color'] = 'red'
            G.edge[0][phone]['width'] = 2
            yield True
            
            G.node[v]['color'] = 'blue'
            G.edge[phone][v]['color'] = 'red'
            G.edge[phone][v]['width'] = 2
            yield True
            
            break

    yield False

def sim2(G, v):
    # Question 2
    nx.set_edge_attributes(G, 'color', 'grey')
    nx.set_edge_attributes(G, 'width', 0.5)
    yield True

    G.node[0]['color'] = 'yellow'
    yield True
    
    for phone in G.neighbors(0):
        if v in G.neighbors(phone):
            G.node[phone]['color'] = 'yellow'
            G.edge[0][phone]['color'] = 'red'
            G.edge[0][phone]['width'] = 2
            yield True
            
            G.node[v]['color'] = 'blue'
            G.edge[phone][v]['color'] = 'red'
            G.edge[phone][v]['width'] = 2
            yield True
            
            break

    yield False

if __name__ == '__main__':
    G = generate()

    u, v = tuple(random.sample(list(range(10, 31)), 2))
    
    genA, genB = sim1(G, u, v), sim2(G, v)
    strA = 'Connecting ' + str(u) + ' to ' + str(v)
    strB = 'External call to ' + str(v)

    position = nx.spring_layout(G)
    for keepGoing in genA:
        pylab.title(strA)
        show(G, setPos=position)
        pylab.pause(0.3)
        if keepGoing != False:
            pylab.cla()
