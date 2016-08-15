class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        flag, res = True, 0
        if not strs:
            return ''
        j = 0
        while True:
            for i in range(len(strs)):
                if j >= len(strs[i]):
                    flag = False
                    break
                elif strs[i][j] != strs[0][j]:
                    flag = False
            j += 1
            if flag == False:
                break
            else:
                res = j
        return strs[0][:res]