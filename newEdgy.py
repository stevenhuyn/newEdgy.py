"""
Set node outline for new matplotlib defaults
ty
https://stackoverflow.com/questions/22716161/how-can-one-modify-the-outline-color-of-a-node-in-networkx

"""

import networkx as nx
import pylab
from collections import deque

# as nx.write_dot doesn't work, workaround
# http://stackoverflow.com/questions/14943439/how-to-draw-multigraph-in-networkx-using-matplotlib-or-graphviz
from networkx.drawing.nx_pydot import write_dot

try:
    from Queue import PriorityQueue
except ImportError:
    from queue import PriorityQueue

# Turns on interactive mode for animation???
# http://stackoverflow.com/questions/12358312/keep-plotting-window-open-in-matplotlib
pylab.ion()

def show(G,
         node_attribute="id",
         edge_attribute="weight",
         node_size=1250,
         setPos=None,
         labelPos=0.7,
         nodeFontSize=12,
         edgeFontSize=12):
    """
    For basic needs
    >> Show(G)

    Parameters
    ---------------
    node_attribute:     Which dictionary the labels for the nodes are using for
                        the label
    edge_attribute:     Same as above but for edges
    node_size:          Self explanatory
    setPos:             Position arry for the nodes, returned from
                        the layout methods example nx.spring_layout
    labelPos:           The offset of the edge labels to avoid overlap defaults
                        0.7 for non symmetry
    nodeFontSize:       ...
    edgeFontSize:       Modify the font size of edges
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
        nx.draw_networkx_labels(G, layout, node_labels, font_size=nodeFontSize)

    if edge_attribute != None:
        edge_labels = dict((e, G.edge[e[0]][e[1]].get(edge_attribute, "")) for e in G.edges())
        nx.draw_networkx_edge_labels(G, layout, edge_labels, label_pos=labelPos, font_size=edgeFontSize)

    pylab.axis('off')
    
    nodes = nx.draw_networkx_nodes(G, layout, node_color=node_colors, node_size=node_size)
    edges = nx.draw_networkx_edges(G, layout, edge_color=edge_colors, width=edge_width)
    
    # If G has no nodes, then this will raise an error :(
    nodes.set_edgecolor('black')

def onPress(event):
    # Adds binds to the matplotlib window so you
    # can close it when focused properly
    if event.key == 'ctrl+d':
        exit()
    elif event.key == 'ctrl+c':
        # kind of a hacky away to pause the generator
        global step
        step = False

def animate(G, gen, **kwargs):
    # Binding
    pylab.gcf().canvas.mpl_connect('key_press_event', onPress)
        
    # There are other layouts, look them up in nx documentation
    position = nx.spring_layout(G)  
    for keepGoing in gen(G, **kwargs):
        # step is the value of the yield statement
        show(G, setPos=position)
        pylab.pause(0.001)
        if keepGoing != False:
            # upon final iteration, yield False so step == false
            # and therefore not clear the graph on final iteration
            pylab.cla()
        else:
##            pylab.ioff()
            pylab.show()
            break

def hierarchy_pos(G, root, levels=None, width=1., height=1.):
    # Legitmate goldmine
    # http://stackoverflow.com/questions/29586520/can-one-get-hierarchical-graphs-from-networkx-with-python-3
    '''If there is a cycle that is reachable from root, then this will see infinite recursion.
       G: the graph
       root: the root node
       levels: a dictionary
               key: level number (starting from 0)
               value: number of nodes in this level
       width: horizontal space allocated for drawing
       height: vertical space allocated for drawing'''
    TOTAL = "total"
    CURRENT = "current"
    def make_levels(levels, node=root, currentLevel=0, parent=None):
        """Compute the number of nodes for each level
        """
        if not currentLevel in levels:
            levels[currentLevel] = {TOTAL : 0, CURRENT : 0}
        levels[currentLevel][TOTAL] += 1
        neighbors = G.neighbors(node)
        if parent is not None:
            neighbors.remove(parent)
        for neighbor in neighbors:
            levels =  make_levels(levels, neighbor, currentLevel + 1, node)
        return levels

    def make_pos(pos, node=root, currentLevel=0, parent=None, vert_loc=0):
        dx = 1/levels[currentLevel][TOTAL]
        left = dx/2
        pos[node] = ((left + dx*levels[currentLevel][CURRENT])*width, vert_loc)
        levels[currentLevel][CURRENT] += 1
        neighbors = G.neighbors(node)
        if parent is not None:
            neighbors.remove(parent)
        for neighbor in neighbors:
            pos = make_pos(pos, neighbor, currentLevel + 1, node, vert_loc-vert_gap)
        return pos
    if levels is None:
        levels = make_levels({})
    else:
        levels = {l:{TOTAL: levels[l], CURRENT:0} for l in levels}
    vert_gap = height / (max([l for l in levels])+1)
    return make_pos({})
            
    
