class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        while int(n/5) != 0:
            total += int(n/5)
            n = n/5
            
        return total