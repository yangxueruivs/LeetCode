class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def countDic(aStr):
            dic = {}
            for i in aStr:
                if not dic.get(i):
                    dic[i] = 1
                else:
                    dic[i] += 1
            return dic
        
        return (countDic(s) == countDic(t))