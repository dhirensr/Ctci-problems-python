class CustomStack:
    """
https://leetcode.com/problems/design-a-stack-with-increment-operation/
    """
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.stack = []
    def push(self, x):
        if not (len(self.stack) == self.maxSize):
            self.stack.append(x)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return -1


    def increment(self, k, val):
        if (len(self.stack) < k):
            self.stack = [j+val for j in self.stack]
        else:
            self.stack =  [j+val for j in self.stack[:k]] + self.stack[k:]


obj = CustomStack(3)
obj.push(1)
obj.push(2)
param_2 = obj.pop()
print(obj.increment(2,5))
