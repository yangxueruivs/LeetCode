#Iteration
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1,2]
        for i in range(n-2):
            res.append(res[i+1]+res[i])
        return res[n-1]
#DynamicProgramming
res = []
def dp(n):
    if res[n-1]> 0:
        return res[n-1]
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        res[n-1] = dp(n-1)+dp(n-2)
        return res[n-1]
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(n):
            res.append(0)
        return dp(n)