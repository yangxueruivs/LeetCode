#Backtracking, dfs, dp
def palindromePartition(p, s, length, n):
    j = 0
    while j < length:
        if p[0][j+n-length] == True:
            if j == length-1:
                yield s[:j+1]
            else:
                for res in palindromePartition(p[j+1:], s[j+1:], len(s[j+1:]), n):
                    yield s[:j+1] + '#' +res
        j += 1
                    
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res, column, n = [], [], len(s)
        p = [[False for i in range(n)]for i in range(n)]
        for l in range(n):
            for i in range(n-l):
                j = i+l
                p[i][j] = (s[i:j+1] == s[i:j+1][::-1])
                
        for i in list(palindromePartition(p, s, n, n)):
            res.append(i.split('#'))
            
        return res