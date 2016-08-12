#2D dp, time limit exceeded.
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, column, n = [], [], len(s)
        p, f = [[False for i in range(n)]for i in range(n)], [[0 for i in range(n)]for i in range(n)]
        if s == s[::-1]:
            return 0
        for l in range(n):
            for i in range(n-l):
                j = i+l
                p[i][j] = (s[i:j+1] == s[i:j+1][::-1])
                if p[i][j] == True:
                    f[i][j] = 0
                else:
                    min = 10000
                    for k in range(i,j):
                        if f[i][k]+f[k+1][j] < min:
                            min = f[i][k]+f[k+1][j]+1
                    f[i][j] = min
        return f[0][n-1]
#1D dp.	
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, column, n = [], [], len(s)
        f = [n-i-1 for i in range(n+1)]
        p = [[False for i in range(n)]for i in range(n)]
        if s == s[::-1]:
            return 0
        for i in range(n)[::-1]:
            for j in range(i,n):
                if s[i] == s[j] and (j - i < 2 or p[i + 1][j - 1]):
                    p[i][j] = True
                    f[i] = min(f[i], f[j+1]+1)
        return f[0]