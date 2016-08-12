class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res = ''
        if numRows == 1 or numRows == 0:
            return s
        elif numRows == 2:
            for i in range((s.__len__()+1)/2):
                res += s[2*i]
            for i in range(s.__len__()/2):
                res += s[2*i+1]
            return res
        columns = 2*(s.__len__()/(numRows-1)+1)
        numList = [[0 for i in range(columns)]for i in range(numRows)]
        count, res = 0, ''
        for i in range(columns):
            if i % 2 == 0:
                j = 0
                while j < numRows and count < s.__len__():
                    numList[j][i] = s[count]
                    j += 1
                    count += 1
            else:
                j = numRows-2
                while j > 0 and count < s.__len__():
                    numList[j][i] = s[count]
                    j -= 1
                    count += 1
        for i in range(numRows):
            for j in range(columns):
                if numList[i][j] != 0:
                    res += numList[i][j]
        return res