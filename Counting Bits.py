#res[2**n+i] = res[i]+1
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0 for i in range(num+1)]
        n, flag = 0, 0
        while True:
            for i in range(2**n,2**(n+1)):
                if i > num:
                    flag = 1
                    break
                else:
                    res[i] = res[i-2**n]+1
            if flag == 1:
                break
            n += 1
        return res