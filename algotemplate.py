"""
Quick template using modified edgy.py for redrawing the
graph with a generator function.

References
http://stackoverflow.com/questions/13437284/animating-network-growth-with-networkx-and-matplotlib
http://stackoverflow.com/questions/6686550/how-to-animate-a-time-ordered-sequence-of-matplotlib-plots
http://stackoverflow.com/questions/12822762/pylab-ion-in-python-2-matplotlib-1-1-1-and-updating-of-the-plot-while-the-pro
"""

from edgy import *

def generate():
    G = nx.Graph()

    # Do stuff here to populate G
    
    return G

def stepFig(G):
    # Whenever you want to redraw the graph
    yield True

    # Throw False to stop redrawing graph
    yield False

def onPress(event):
    # OPTIONAL
    
    # Adds binds to the matplotlib window so you
    # can close it when focused properly
    if event.key == 'ctrl+d':
        exit()
    elif event.key == 'ctrl+c':
        # kind of a hacky away to pause the generator
        global step
        step = False
        
if __name__ == '__main__':
    # Binds - OPTIONAL
    pylab.gcf().canvas.mpl_connect('key_press_event', onPress)
    
    G = generate()

    # There are other layouts, look them up in nx documentation
    position = nx.spring_layout(G)  
    for keepGoing in stepFig(G):
        # step is the value of the yield statement
        show(G, setPos=position)
        pylab.pause(0.001)
        if keepGoing != False:
            # upon final iteration, yield False so step == false
            # and therefore not clear the graph on final iteration
            pylab.cla()
