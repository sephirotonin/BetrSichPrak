class EVENT:
    def __init__(self, name, l):
        self.name = name
        self.l = l
    def add(self, node):
        l.append(node)
        return self.nodes
    def failure_probability(self):
        self.fail = self.l
        return self.fail

class NOTNODE:
    def __init__(self, name):
        self.name = name
        self.nodes=[]
    def add(self, node):
        self.nodes.append(node)
        return self.nodes
    def failure_probability(self):
        for i in self.nodes:
            self.fail = 1 - i.failure_probability()
        return self.fail

class ORNODE:
    def __init__(self, name):
        self.name = name
        self.nodes = []
    def add(self, node):
        self.nodes.append(node)
        return self.nodes
    def failure_probability(self):
        prepfail = 1
        for i in self.nodes:
            prepfail *= (1 - i.failure_probability())
        self.fail = 1 - prepfail
        return self.fail 

class ANDNODE:
    def __init__(self, name):
        self.name = name
        self.nodes = []
    def add(self, node):
        self.nodes.append(node)
        return self.nodes
    def failure_probability(self):
        self.fail = 1
        for i in self.nodes:
            self.fail *= i.failure_probability()
        return self.fail

# Aufgabe a)

TOP = ANDNODE("TOP")
A = ORNODE("A")
E1 = EVENT("1",0.1)
E2 = EVENT("2",0.1)
E3 = EVENT("3",0.1)
TOP.add(A)
TOP.add(E1)
A.add(E2)
A.add(E3)

# Aufgabe b)

K1 = ANDNODE("K1")
K2 = ANDNODE("K2")
K3 = ORNODE("K3")
K4 = ANDNODE("K4")
K5 = ORNODE("K5")
Knotty = NOTNODE("Knotty")
A = EVENT("A",0.01)
B = EVENT("B",0.1)
C = EVENT("C",0.001)
D = EVENT("D",0.01)
E = EVENT("E",0.01)
F = EVENT("F",0.01)
G = EVENT("G",0.1)
K1.add(K2)
K1.add(Knotty)
K2.add(D)
K2.add(E)
K2.add(K4)
Knotty.add(K3)
K3.add(F)
K3.add(G)
K4.add(K5)
K4.add(C)
K5.add(A)
K5.add(B)
print(K1.failure_probability())

# c)
import graphviz
import matplotlib

class GraphPrint:
    def __init__(self, name):
        self.name = name
        self.graph = graphviz.Digraph('tree')

    def create(self, top):
        for i in top.nodes:
            self.graph.edge(top.name, i.name)
            if type(i) != EVENT:
                self.create(i)
        
    def view(self):
        self.graph.render(directory='doctest-output').replace('\\', '/')
        'doctest-output/tree.gv.svg'
        self.graph.render(directory='doctest-output', view=True)

TOP = GraphPrint("TOP")

TOP.create(K1)

TOP.view()


#Aufgabe d)

import numpy as np
from matplotlib import pyplot as plt

mean_value = [0.01, 0.1, 0.001, 0.01, 0.01, 0.01, 0.1]
standard_deviation = [0.002, 0.02, 0.002, 0.002, 0.002, 0.002, 0.02]

def normal_distribution():
    liste =[]
    for i in range(999):
        A.l = np.random.normal(loc=mean_value[0], scale=standard_deviation[0])
        B.l = np.random.normal(loc=mean_value[1], scale=standard_deviation[1])
        C.l = np.random.normal(loc=mean_value[2], scale=standard_deviation[2])
        D.l = np.random.normal(loc=mean_value[3], scale=standard_deviation[3])
        E.l = np.random.normal(loc=mean_value[4], scale=standard_deviation[4])
        F.l = np.random.normal(loc=mean_value[5], scale=standard_deviation[5])
        G.l = np.random.normal(loc=mean_value[6], scale=standard_deviation[6])

        if A.l<0:
            A.l = A.l * (-1)
        if B.l<0:
            B.l = B.l * (-1)
        if C.l<0:
            C.l = C.l * (-1)
        if D.l<0:
            D.l = D.l * (-1)
        if E.l<0:
            E.l = E.l * (-1)
        if F.l<0:
            F.l = F.l * (-1)
        if G.l<0:
            G.l = G.l * (-1)
        
        liste.append(K1.failure_probability())

    plt.hist(liste, 30)
    plt.xlabel("failure probability")
    plt.ylabel("n")

    return plt.show()

normal_distribution()