#KMP-related
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        else:
            res = s[0]
            result = res
            for i in range(1,len(s)):
                if res.find(s[i]) == -1:
                    res += s[i]
                else:
                    if len(res) > len(result):
                        result = res
                    j = res.index(s[i])
                    res = s[(i-len(res)+j)+1:i+1]
            if len(res) > len(result):
                result = res
            return len(result)
            