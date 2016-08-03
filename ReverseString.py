#StringProcessing
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        out = []
        for i in range(len(s), 0, -1):
            out.append(s[i-1])
        return "".join(out)