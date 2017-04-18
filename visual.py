
from newEdgy import *
import itertools

def buildFull(G, a, b):
    G.add_node(a)
    G.node[a]['predecessor'] = None
    queue = [a]
    seen = set([a])
    while queue != []:
        u = queue[0]
        queue.pop(0)
        for v in possibleMoves(u):
            if v in seen:
                continue
            G.add_edge(u, v)
            G.node[v]['predecessor'] = u
            seen.add(v)
            if isLegal(u, v):
                queue.append(v)
    return G

def possibleMoves(u):
        people, side = u[:-1], u[-1]
        
        # Viable riders (people on same side as motorbike)
        riders = [ i for i, n in enumerate(people) if n == side ]

        # Generating every combination of riders to be flipped to the other side
        pairs = comboTwo(riders)
        solo = [ (i,) for i in riders ]

        # indexes are the riders that flip to the other side        
        for index in itertools.chain(solo, pairs):
            v = ''
            for i, n in enumerate(people):
                if i in index:
                    v += inverse(n)
                else:
                    v += n
            v += inverse(side)  # Moving motorbike to other side
            yield v

def comboTwo(l):
    for i in range(len(l)):
        for j in range(i, len(l)):
            yield l[i], l[j]
            
def isLegal(u, v):
    conds = []

    # Motorbike ride 
    group = []
    for i, (cu, cv) in enumerate(zip(u[:-1], v[:-1])):
        if cu != cv:
            group.append(i)
            
    return not any([group == [0, 3], group == [1, 2],   # Motorbike ride is legal
                v[:-1] == '0110', v[:-1] == '1001'])    # v is legal

def inverse(u):
    s = ''
    for c in u:
       s += str(int(not int(c)))
    return s

def colorise(G, b):
    u = b
    v = G.node[u]['predecessor']
    while v != None:
        highlight(G, u, v)
        u = v
        v = G.node[u]['predecessor']


def highlight(G, u, v):
    print(u, v)
    G.add_edge(u, v, color='blue', width=3)

if __name__ == '__main__':
    a, b = '00000', '11111'
    G = nx.Graph()
    buildFull(G, a, b)
    colorise(G, b)
    show(G, setPos=hierarchy_pos(G, a))
