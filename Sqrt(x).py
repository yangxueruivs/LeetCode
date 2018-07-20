class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        elif x == 1 or x == 2:
            return 1
        
        r = x
        while r*r > x:
            r = int(r/2)
        while r*r <= x:
            r += 1
        return r - 1    