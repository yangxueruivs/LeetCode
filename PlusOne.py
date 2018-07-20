class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = "".join(map(str,digits))
        res = list(str(int(s)+1))
        return [int(i) for i in res]