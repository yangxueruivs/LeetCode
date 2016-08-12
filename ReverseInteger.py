class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = str(x)
        if x > 0:
            res = res[::-1].strip('0')
        elif x < 0:
            res = '-' + res.strip('-')[::-1].strip('0')
        else:
            res = 0
        if int(res) >= 2147483647 or int(res) <= -2147483648:
            return 0
        else:
            return int(res)