#dp, O(n)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        diff, n = [], len(prices)
        if n <= 1:
            return 0
        for i in range(1,n):
            diff.append(prices[i]-prices[i-1])
        res = [diff[i] for i in range(len(diff))]
        out = res[0]
        for i in range(1,len(diff)):
            res[i] = max(res[i-1]+diff[i],diff[i])
            if res[i] > out:
                out = res[i]
        if out <= 0:
            return 0
        return out
#Greedy, O(n)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        diff, n, res= [], len(prices), 0
        if n <= 1:
            return 0
        minPrice = prices[0]
        for i in range(1,n):
            res = max(res, prices[i]-minPrice)
            minPrice = min(minPrice, prices[i])
        return res
        