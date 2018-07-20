class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        temp = bin(n)[2:]
        temp = list((32 - len(temp))*'0' + temp)
        temp.reverse()
        temp = "".join(temp)
        
        return int(temp, 2)