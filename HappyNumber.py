from functools import reduce

class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def mapHappy(num):
            return int(num)**2
        
        def reduceHappy(a, b):
            return int(a) + int(b)
        
        count = 0
        
        while count <= 100:
            temp = list(str(n))
            res = reduce(reduceHappy, map(mapHappy, temp))
            if res == 1:
                return True
            n = res
            count += 1
        
        return False
                