class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res, numList, dic = '', [], {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        
        keysList = dic.keys()
        keysList.sort(reverse=True)
        for i in keysList:
            if num/i >= 1:
                res += dic[i]*(num/i)
                num %= i
        return res