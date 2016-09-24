#stack
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str1, stack, dic = '([{', [], {'(':')', '[':']', '{':'}'}
        for i in s:
            if str1.find(i) > -1:
                stack += i
            elif len(stack) == 0 or dic[stack[-1]] != i:
                return False
            else:
                del stack[-1]
        if len(stack) == 0:
            return True
        else:
            return False