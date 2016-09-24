class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        diffs, n, out = [], len(prices), 0
        if n <= 1:
            return 0
        for i in range(1,n):
            diffs.append(prices[i]-prices[i-1])
        for diff in diffs:
            if diff > 0:
                out += diff
        return out