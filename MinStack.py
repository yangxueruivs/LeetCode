class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.vals = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.vals += [x]

    def pop(self):
        """
        :rtype: void
        """
        res = self.vals[-1]
        del self.vals[-1]
        return res

    def top(self):
        """
        :rtype: int
        """
        return self.vals[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.vals) 


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()