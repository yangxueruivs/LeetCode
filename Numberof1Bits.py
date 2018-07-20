class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        res = str(bin(n))
        for i in res:
            if i == '1':
                count += 1
                
        return count