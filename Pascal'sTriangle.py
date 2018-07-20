from numpy import *

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        
        if numRows == 0:
            return res
        elif numRows == 1:
            res = [[1]]
            return res
        elif numRows == 2:
            res = [[1], [1, 1]]
            return res
        
        res = [[1], [1, 1]]
        for i in range(2, numRows):
            temp = []
            temp += [res[i-1][0]]
            for j in range(1, i):
                temp += [res[i-1][j-1]+res[i-1][j]]
            temp += [res[i-1][-1]]
            res.append(temp)
        return res