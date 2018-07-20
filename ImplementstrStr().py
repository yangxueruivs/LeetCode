class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = 0
        while haystack[i:i+len(list(needle))] != needle:
            i += 1
            if i+len(list(needle)) > len(list(haystack)):
                return -1
        return i