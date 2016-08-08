#Manacher Method, O(n)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxI, maxL, n, index= 1, 0, len(s), 1
        p = [1 for i in range(2*n+1)]
        if s == s[::-1]:
            return s
        for i in range(n-1):
            s = s[:2*i+1]+'#'+s[2*i+1:]
        s = '*' + s + '#'
        
        for i in range(2, 2*n):
            if maxI + p[maxI] > i:
                p[i] = min(p[2*maxI-i], p[maxI]-i+maxI)
            else:
                p[i] = 1
                
            r = 1
            while i+r <= 2*n and s[i+r] == s[i-r]:
                p[i] = r
                r += 1
            if maxI+p[maxI] < i+p[i]:
                maxI = i
            if maxL < p[i]:
                maxL = p[i]
                index = i
        res = s[index-maxL:index+maxL+1].strip('*').replace('#','')
        
        return res
#dp time limit exceeded
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        startIndex, endIndex, n = 0, 0, len(s)
        f = [[False for count1 in range(n)] for count2 in range(n)]
        for k in range(n):
            f[k][k] = True
        if n == 0:
            return s
        for l in range(1,n):
            for i in range(n-l):
                j = i+l
                f[i][j] = s[i] == s[j] and (f[i+1][j-1] if j != i+1 else True)
                if f[i][j] == True:
                    if endIndex-startIndex < j-i:
                        endIndex, startIndex = j, i
        return s[startIndex:endIndex+1]