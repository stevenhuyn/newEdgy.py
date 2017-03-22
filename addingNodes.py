"""
What happens if you continually add nodes
"""

from newEdgy import *

def generate():
    G = nx.Graph()

    # Do stuff here to populate G

    return G

def stepFig(G):
    # Whenever you want to redraw the graph
    for i in range(100):
        G.add_edge(i, i + 1)
        G.node[i + 1]['Position'] = (0, 10)
        yield True
    
    # Throw False to stop and not clear the final draw
    yield False

def onPress(event):
    # Adds binds to the matplotlib window so you
    # can close it when window focused
    if event.key == 'ctrl+d':
        exit()
    elif event.key == 'ctrl+c':
        # Hacky way to stop the animation
        global keepGoing
        keepGoing = False
    elif event.key == 'ctrl+z':
        # Restart the animation
        main()

def main():
    pylab.gcf().canvas.mpl_connect('key_press_event', onPress)
    
    G = generate()

    position = nx.spring_layout(G)
    for keepGoing in stepFig(G):
        show(G, setPos=position)
        pylab.pause(0.001)
        if keepGoing != False:
            # Clears the graph
            pylab.cla()
        else:
            # Does not clear the graph
            pylab.ioff()
            pylab.show()
            break

if __name__ == '__main__':
    main()
