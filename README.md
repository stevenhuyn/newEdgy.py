# newEdgy.py
Helper function to quickly draw small networkx graphs, with some extended functions to aid animation.  
Based off of the edgy.py file from the VCE Algorithmic course 2017.  
For networkx, matplotlib 2.0 and python 3.5+.

**Usage**  
Only file necessary is newEdgy.py

```Python
>> from newEdgy import *
>> G = nx.Graph()
>> G.add_nodes_from([1, 2, 3])
>> G.node[2]['color'] = 'red'
>> show(G)
```

**Animations**  
Run your scripts through python's interactive mode to be able to modify plots on the fly, and is required for the animate function. look at minimalTemplate.py for the quickest and dirtiest way to animate/convert existing algorithms.

cli example  
python -i script.py

**Links to references**  
Setting outline of nodes in networkx  
https://stackoverflow.com/questions/22716161/how-can-one-modify-the-outline-color-of-a-node-in-networkx

Using pylab.ion()  
http://stackoverflow.com/questions/12358312/keep-plotting-window-open-in-matplotlib

Animation  
http://stackoverflow.com/questions/13437284/animating-network-growth-with-networkx-and-matplotlib
http://stackoverflow.com/questions/6686550/how-to-animate-a-time-ordered-sequence-of-matplotlib-plots
http://stackoverflow.com/questions/12822762/pylab-ion-in-python-2-matplotlib-1-1-1-and-updating-of-the-plot-while-the-pro
