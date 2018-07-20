class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        p = [True]*n
        p[0] = p[1] = False
        p[2] = True
        
        for i in range(2, n):
            if p[i]:
                p[2*i:n:i] = [False]*len(p[2*i:n:i])
        
        return sum(p)