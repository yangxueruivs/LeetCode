class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numList, dic = [], {'I':1, 'X':10, 'C':100, 'M':1000, 'V':5, 'L':50, 'D':500}
        for i in s:
            numList.append(dic[i])
        
        res = 0
        while numList:
            id = numList.index(max(numList))
            temp = 0
            if numList.index(max(numList)) != 0:
                for i in range(id):
                    temp += numList[i]
                res += (max(numList)-temp)
            else:
                res += max(numList)
            numList = numList[id+1:]
        return res
            
            