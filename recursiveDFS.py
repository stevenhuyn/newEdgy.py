"""
An example of animating a recursive algorithm.
"""

from newEdgy import *
import random

def recDFS(G, u, prev=None):
    
    if G.node[u]['marked'] == False:
        G.node[u]['count'] = G.count
        G.node[u]['prev'] = prev
        G.count += 1
        G.node[u]['cat'] = str(u) + ' - ' + str(G.count)
    else:
        return
        
    G.node[u]['marked'] = True
    G.node[u]['color'] = 'green'
    viable = [ n for n in G[u] if G.node[n]['marked'] == False ]
    
    if len(viable) != 0:
        for node in viable:
            yield True
            yield from recDFS(G, node, prev=u)      # MAGIC???

    if prev == None:
        # Only first call will end with a yield False
        yield False

def recAnimate():
    u = random.choice(G.nodes())
    for step in recDFS(G, u):
        show(G, setPos=position)
        pylab.pause(0.001)
        if step != False:
            pylab.cla()

def showPath():
    recDFS(G, 0)

    for v in sorted(G, key=lambda n: G.node[n]['count']):
        show(G, setPos=position)
        pylab.pause(0.001)
        pylab.cla()
        u = G.node[v]['prev']
        if u == None:
            G.node[v]['color'] = 'cyan'
            continue
        G.edge[u][v]['color'] = 'red'
        G.edge[u][v]['width'] = 2

    show(G, setPos=position)
    pylab.pause(0.001)
    pylab.cla()

    for u, v in G.edges():
        if G.edge[u][v]['color'] == 'grey':
            G.edge[u][v]['color'] = 'white'

    show(G, setPos=position, node_attribute='count')
    pylab.pause(0.001)

if __name__ == '__main__':
    # Preliminary
    G = nx.grid_graph([3, 5])
    G.count = 0
    position = nx.spring_layout(G)
    
    nx.set_edge_attributes(G, 'width', 0.5)
    nx.set_edge_attributes(G, 'color', 'grey')
    
    nx.set_node_attributes(G, 'prev', None)
    nx.set_node_attributes(G, 'marked', False)

    recAnimate()
    pylab.cla()
    showPath()
