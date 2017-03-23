"""
Visualising the MHS PBX system
"""

from newEdgy import *
import random

def generate():
    nodeListPBX = [0]
    nodeListPhone = list(range(1, 10))
    nodeListStaff = list(range(10, 31))
    
    edgeListConnects = ((0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8),
                        (0, 9))
    edgeListNear = ((1, 10), (2, 11), (2, 12), (2, 13), (2, 14), (3, 15), (3, 16),
                    (3, 17), (3, 18), (4, 19), (4, 20), (5, 21), (6, 22), (6, 23),
                    (7, 24), (7, 25), (7, 26), (8, 27), (8, 28), (9, 29), (9, 30))
    
    G = nx.Graph()
    G.add_nodes_from(nodeListPBX + nodeListPhone + nodeListStaff)
    G.add_edges_from(edgeListConnects + edgeListNear)

    return G

def ConnectAndColour(G, u, v, col):
    """ colours the edge u to v and node v to col """
    G.add_edge(u, v)    # In case not connected
    G.edge[u][v]['color'] = 'red'
    G.edge[u][v]['width'] = 2
    G.node[v]['color'] = col

def sim1(G, u, v):
    """ Simulating a call between to staff members u and v """
    nx.set_edge_attributes(G, 'color', 'grey')
    nx.set_edge_attributes(G, 'width', 0.5)
    yield True

    G.node[u]['color'] = 'green'
    yield True

    # As each staff only has 1 neighbour,
    # Below is the fastest way to get a arbitary key from a dict
    firstPhone = next(iter(G[u].keys()))
    
    # Checks if the staff nodes are connected by the same phone
    if v in G[firstPhone]:
        # That means they can just talk to eachother without the PBX system
        ConnectAndColour(G, u, v, 'blue')
    else:
        # Otherwise, run as normal
        ConnectAndColour(G, u, firstPhone, 'yellow')
        yield True

        ConnectAndColour(G, firstPhone, 0, 'yellow')
        yield True

        # Finding which phone extension contains v
        # then connecting and then breaking the loop
        for phone in G[0]:
            if v in G[phone]:
                ConnectAndColour(G, 0, phone, 'yellow')
                yield True

                ConnectAndColour(G, phone, v, 'blue')
                yield True
                
                break
    print('ended')
    yield False

def sim2(G, v):
    """ Simluating an external call through the PBX system to v """
    nx.set_edge_attributes(G, 'color', 'grey')
    nx.set_edge_attributes(G, 'width', 0.5)
    yield True

    G.node[0]['color'] = 'yellow'
    yield True

    # Checking phone neighbours of PBX to see if the phone contains v
    for phone in G[0]:
        if v in G[phone]:
            ConnectAndColour(G, 0, phone, 'yellow')
            yield True

            ConnectAndColour(G, phone, v, 'blue')
            yield True
            
            break

    yield False

def main():
    print('test')
    pylab.gcf().canvas.mpl_connect( 'key_press_event', onPress)
    
    G = generate()
    
    u, v = tuple(random.sample(list(range(10, 31)), 2))
    genA = sim1(G, u, v)
    genB = sim2(G, v)
    strA = 'Connecting ' + str(u) + ' to ' + str(v)
    strB = 'External call to ' + str(v)

    position = nx.spring_layout(G)
    for keepGoing in genA:
        pylab.title(strA)
        show(G, setPos=position, labelPos=0.5)
        pylab.pause(0.0001)
        if keepGoing != False:
            pylab.cla()
        else:
            pylab.ioff()
            pylab.show()
            break
        
if __name__ == '__main__':
    main()

