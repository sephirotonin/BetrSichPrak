class EVENT:
    def __init__(self, name, l):
        self.name = name
        self.l = l
        #self.l = []
        #self.l.append(l)
        #...
    def add(self, node):
        l.append(node)
        return
    def failure_probability(self):
        #...
        return self.failure_probability

class NOTNODE:
    def __init__(self, name):
        self.name = name
        self.nodes=[]
    def add(self, node):
        self.nodes.append(node)
        return
    def failure_probability(self):
        #...
        return self.fail

class ORNODE:
    def __init__(self, name):
        self.name = name
        self.nodes = []
    def add(self, node):
        self.nodes.append(node)
        return
    def failure_probability(self):
        #...
        return self.fail 

class ANDNODE:
    def __init__(self, name):
        self.name = name
        self.nodes = []
    def add(self, node):
        self.nodes.append(node)
        return
    def failure_probability(self):
        #...
        return self.fail 

TOP = ANDNODE("TOP")
A = ORNODE("A")
E1 = EVENT("1",0.1)
E2 = EVENT("2",0.1)
E3 = EVENT("3",0.1)
TOP.add(A)
TOP.add(E1)
A.add(E2)
A.add(E3)