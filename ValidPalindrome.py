class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j, flag = 0, len(s)-1, True
        while i <= j:
            if (s[i].isalpha() or s[i].isdigit()) and (s[j].isalpha() or s[j].isdigit()):
                if s[i].lower() != s[j].lower():
                    flag = False
                    break
                else:
                    i += 1
                    j -= 1
            elif not (s[i].isalpha() or s[i].isdigit()):
                i += 1
            elif not (s[j].isalpha() or s[j].isdigit()):
                j -= 1
            if i == j:
                break
        return flag