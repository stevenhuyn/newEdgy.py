"""
Visualising the MHS PBX system
"""
from edgy import *
import random

def generate():
    nodeList = list(range(31))
    edgeList = ((0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8),
                (0, 9), (1, 10), (2, 11), (2, 12), (2, 13), (2, 14), (3, 15),
                (3, 16), (3, 17), (3, 18), (4, 19), (4, 20), (5, 21), (6, 22),
                (6, 23), (7, 24), (7, 25), (7, 26), (8, 27), (8, 28), (9, 29),
                (9, 30))
    
    G = nx.Graph()
    G.add_nodes_from(nodeList)
    G.add_edges_from(edgeList)

    return G

def ConnectAndColour(G, u, v, col):
    """ colours the edge u to v and colours node v to col """
    G.add_edge(u, v)
    G.edge[u][v]['color'] = 'red'
    G.edge[u][v]['width'] = 2
    G.node[v]['color'] = col

def sim1(G, u, v):
    """ Question 1
    u, v are staff nodes
    """
    nx.set_edge_attributes(G, 'color', 'grey')
    nx.set_edge_attributes(G, 'width', 0.5)
    yield True

    G.node[u]['color'] = 'green'
    yield True

    firstPhone = G.neighbors(u)[0]
    # Checks if the staff nodes are connected by the same phone
    if G.neighbors(v)[0] == firstPhone:
        # That means they can just talk to eachother without the PBX system
        ConnectAndColour(G, u, v, 'blue')
    else:
        # Otherwise, run as normal
        ConnectAndColour(G, u, firstPhone, 'yellow')
        yield True

        ConnectAndColour(G, firstPhone, 0, 'yellow')
        yield True

        # Checking phone neighbours of PBX to see if the phone contains v
        for phone in G.neighbors(0):
            if v in G.neighbors(phone):
                ConnectAndColour(G, 0, phone, 'yellow')
                yield True

                ConnectAndColour(G, phone, v, 'blue')
                yield True
                
                break

    yield False

def sim2(G, v):
    """ Question 2
    v is the node that will be connected to

    A cut and paste of simulation but removes the initial part of connecting
    to the PBX from u
    """
    nx.set_edge_attributes(G, 'color', 'grey')
    nx.set_edge_attributes(G, 'width', 0.5)
    yield True

    G.node[0]['color'] = 'yellow'
    yield True

    # Checking phone neighbours of PBX to see if the phone contains v
    for phone in G.neighbors(0):
        if v in G.neighbors(phone):
            ConnectAndColour(G, 0, phone, 'yellow')
            yield True

            ConnectAndColour(G, phone, v, 'blue')
            yield True
    
            break

    yield False

def onPress(event):
    # Just for ease of use
    if event.key == 'ctrl+d':
        exit()
    elif event.key == 'ctrl+c':
        global step
        step = False
    elif event.key == 'ctrl+z':
        # Restarts main loop
        pylab.cla()
        main()

def main():
    pylab.gcf().canvas.mpl_connect('key_press_event', onPress)
    
    G = generate()

    # Randomly selects 2 staff nodes
    u, v = tuple(random.sample(list(range(10, 31)), 2))
    
    genA = sim1(G, u, v)
    genB = sim2(G, v)

    strA = 'Connecting ' + str(u) + ' to ' + str(v)
    strB = 'External call to ' + str(v)

    position = nx.spring_layout(G)
    for keepGoing in genA:
        pylab.title(strA)
        show(G, setPos=position)
        pylab.pause(0.0001)
        if keepGoing != False:
            pylab.cla()
        else:
            break
        
if __name__ == '__main__':
    main()
