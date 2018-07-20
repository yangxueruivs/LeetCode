class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        
        dic = {}
        ss = list(s).copy()
        for i in s:
            if dic.get(i):
                dic[i] += 1
            else:
                dic[i] = 1
        
        s, i = list(s), 0
        for i in range(len(s)):
            if dic.get(s[i]) == 1:
                return i
            
        return -1