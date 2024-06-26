import numpy as np
import graphviz
import matplotlib

class STATE:
    def __init__(self, name, num):
        self.name = name
        self.num = num
        return 

class TRANSITION:
    def __init__(self, source, destination, name, rate):
        self.source = source
        self.destination = destination
        self.name = name
        self.rate = rate
        return

class MARKOV:
    def __init__(self, name, dt=1.0):
        self.nodes = []
        self.transitions= []
        self.name = name
    def state(self, name):
        self.nodes.append(name)
        return self.nodes
    def transition(self, name):
        self.transitions.append(name)
        return self.transitions
    def probability(self, p0, wdh, n):
        s = (n,n)
        m = np.zeros(s)

        l =[]
        l_rate = []
        for i in self.transitions:
            part = [x for x in i.name.split()]
            l.append(part)
            l_rate.append(i.rate)

        l_erster_index = []
        for i in l:
            for e in i:
                l_erster_index.append(int(e[0]))

        l_zweiter_index = []
        for i in l:
            for e in i:
                l_zweiter_index.append(int(e[1]))

        a = [i for i in l_erster_index]
        b = [j for j in l_zweiter_index]
        r = [k for k in l_rate]
        
        for y in range(len(l_erster_index)):
            m[a,b] = r

        for i in range(wdh):
            p0 = np.dot(p0, m)
        print("Summe der Wahrscheinlichkeiten " + str(p0.sum()))
        return p0
    
    def plotMarkov(self):
        self.graph = graphviz.Digraph('tree')

        for i in self.transitions:
            self.graph.edge(i.source.name, i.destination.name)

        self.graph.render(directory='doctest-output').replace('\\', '/')
        'doctest-output/tree.gv.svg'
        self.graph.render(directory='doctest-output', view=True)
        return

M = MARKOV("Beispiel")
S1 = STATE('S1',0)
S2 = STATE('S2',1)
S3 = STATE('S3',2)
M.state(S1)
M.state(S2)
M.state(S3)
T12 = TRANSITION(S1, S2, 'l12', 1000)
T13 = TRANSITION(S1, S3, "l11", 1000)
T31 = TRANSITION(S3, S1, 'l31', 1000)
M.transition(T12)
M.transition(T13)
M.transition(T31)


#M.plotMarkov()

A = MARKOV("Aufgabe3")
Z0 = STATE("Z0", 0)
Z1 = STATE("Z1", 1)
Z2 = STATE("Z2", 2)
Z3 = STATE("Z3", 3)
Z4 = STATE("Z4", 4)
Z5 = STATE("Z5", 5)
A.state(Z0)
A.state(Z1)
A.state(Z2)
A.state(Z3)
A.state(Z4)
A.state(Z5)
lambda1 = 3000/1000000000 #FIT -> 1/h
h = 1/8
T00 = TRANSITION(Z0, Z0, "00", 1 - 4 * lambda1) 
T01 = TRANSITION(Z0, Z1, "01", 2 * lambda1)
T11 = TRANSITION(Z1, Z1, "11", 1 - ((2 * lambda1)+h))
T10 = TRANSITION(Z1, Z0, "10", h)
T04 = TRANSITION(Z0, Z4, "04", 2 * lambda1)
T21 = TRANSITION(Z2, Z1, "21", h)
T12 = TRANSITION(Z1, Z2, "12", lambda1) 
T22 = TRANSITION(Z2, Z2, "22", 1 - h)
T13 = TRANSITION(Z1, Z3, "13", lambda1)
T33 = TRANSITION(Z3, Z3, "33", 1 - lambda1) 
T34 = TRANSITION(Z3, Z4, "34", lambda1)
T43 = TRANSITION(Z4, Z3, "43", lambda1)
T44 = TRANSITION(Z4, Z4, "44", 1 - 2 * lambda1)
T45 = TRANSITION(Z4, Z5, "45", lambda1)
T55 = TRANSITION(Z5, Z5, "55", 1 - 0)
A.transition(T00)
A.transition(T01)
A.transition(T11)
A.transition(T10)
A.transition(T04)
A.transition(T21)
A.transition(T12)
A.transition(T22)
A.transition(T13)
A.transition(T33)
A.transition(T34)
A.transition(T43)
A.transition(T44)
A.transition(T45)
A.transition(T55)
A.plotMarkov()

p0 = np.array([1,0,0,0,0,0])

print("Für 40 Tage: " + str(A.probability(p0,960,6)) + "\n")
print("Für 0.5 Jahre: " + str(A.probability(p0,4380,6)) + "\n")
print("Für 12 Jahre: " + str(A.probability(p0,105120,6)) + "\n")
print("Für 40 Jahre: " + str(A.probability(p0,2 * 105120,6)) + "\n")
