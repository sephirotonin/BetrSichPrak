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