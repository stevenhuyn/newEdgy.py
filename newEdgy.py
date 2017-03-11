"""
Set node outline for new matplotlib defaults
ty
https://stackoverflow.com/questions/22716161/how-can-one-modify-the-outline-color-of-a-node-in-networkx

"""

import networkx as nx
import pylab
from collections import deque

try:
    from Queue import PriorityQueue
except ImportError:
    from queue import PriorityQueue

# Turns on interactive mode
# http://stackoverflow.com/questions/12358312/keep-plotting-window-open-in-matplotlib ty
pylab.ion()

def show(G, node_attribute = "id", edge_attribute = "label", node_size=1250,
         setPos=None, labelPos=0.7):
    """
    node_attribute:     Which dictionary the labels for the nodes are using for
                        the label
    edge_attribute:     Same as above but for edges
    node_size:          Self explanatory
    setPos:             Position arry for the nodes, returned from
                        the layout methods example nx.spring_layout
    labelPos:           The offset of the edge labels to avoid overlap defaults
                        0.7 for non symmetry
    """

    if setPos == None:
        # If position doesn't matter generate spring layout
        layout = nx.spring_layout(G)
    else:
        # If position already set aka for animation
        layout = setPos

    for v, data in G.nodes(data = True):
        if "x" in data:
            layout[v] = [data["x"], layout[v][1]]
        if "y" in data:
            layout[v] = [layout[v][0], data["y"]]

    node_colors = [G.node[v].get("color", "white") for v in G.nodes()]
    edge_colors = [G.edge[e[0]][e[1]].get("color", "black") for e in G.edges()]
    edge_width = [G.edge[e[0]][e[1]].get("width", 1) for e in G.edges()]
    

    if node_attribute != None:
        node_labels = dict((v, v if node_attribute == "id" else G.node[v].get(node_attribute, v))
            for v in G.nodes())
        nx.draw_networkx_labels(G, layout, node_labels)

    if edge_attribute != None:
        edge_labels = dict((e, G.edge[e[0]][e[1]].get(edge_attribute, "")) for e in G.edges())
        nx.draw_networkx_edge_labels(G, layout, edge_labels, label_pos=labelPos)

    pylab.axis('off')
    
    nodes = nx.draw_networkx_nodes(G, layout, node_color = node_colors, node_size=node_size)
    edges = nx.draw_networkx_edges(G, layout, edge_color=edge_colors, width=edge_width,
                                   node_edge='black')
    
    # If G has no nodes, then this will raise an error :(
    nodes.set_edgecolor('black')
