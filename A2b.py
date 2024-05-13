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

TOP = ANDNODE("TOP")
A = ORNODE("A")
E1 = EVENT("1",0.1)
E2 = EVENT("2",0.1)
E3 = EVENT("3",0.1)
TOP.add(A)
TOP.add(E1)
A.add(E2)
A.add(E3)
print(TOP.failure_probability())