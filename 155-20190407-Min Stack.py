class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = []
        self.size = 0

    # @param x, an integer
    # @return nothing
    def push(self, x):
        if self.size == 0:
            self.min.append(x)
        else:
            if x <= self.min[-1]:
                self.min.append(x)
        self.stack.append(x)
        self.size += 1

    # @return nothing
    def pop(self):
        tmp = self.stack.pop()
        self.size -= 1
        if tmp == self.min[-1]:
            self.min.pop()

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        return self.min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()