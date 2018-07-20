class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        sequence = '1'
        for i in range(n-1):
            temp = sequence
            sequence = ""
            for num, times in itertools.groupby(temp):
                digitLength = len(list(times))
                sequence += (str(digitLength) + str(num))
        return sequence