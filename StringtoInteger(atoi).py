class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        flag, res = False, ''
        if str == '':
            return 0
        for i in str:
            if i.isdigit():
                res += i
            elif flag == False and (i == '+' or i == '-'):
                flag = True
                res += i
            else:
                break
        if res.isdigit() or (len(res) > 1 and (res[0] == '-' or res[0] == '+') and res[1:].isdigit()):
            if int(res)>=2147483647:
                return 2147483647
            elif int(res)<=-2147483648:
                return -2147483648
            else:
                return int(res)
        else:
            return 0