class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        total = 0
        for i in range(length):
            total += (ord(list(s)[i]) - 64)*(26**(length-i-1))
            
        return total