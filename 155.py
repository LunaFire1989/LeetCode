class MinStack(object):

    def __init__(self):
        self.s1 = []
        self.s2 = []   

    def push(self, x):
        self.s1.append(x)
        if len(self.s2) == 0 or x <= self.s2[-1]:
            self.s2.append(x)

    def pop(self):
        if len(self.s1) == 0:
            return
        x = self.s1[-1]
        self.s1.pop()
        if len(self.s2) != 0 and self.s2[-1] == x:
            self.s2.pop()

    def top(self):
        if len(self.s1) == 0:
            return 0
        return self.s1[-1]

    def getMin(self):
        if len(self.s2) == 0:
            return 0
        return self.s2[-1]
        
obj = MinStack()
obj.push(5)
obj.push(10)
x = obj.top()
print x
x = obj.getMin()
print x