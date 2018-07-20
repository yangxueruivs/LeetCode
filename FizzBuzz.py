class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1, n+1):
            if i%3 == 0:
                if i%5 == 0:
                    res += ['FizzBuzz']
                else:
                    res += ['Fizz']
            elif i%5 == 0:
                res += ['Buzz']
            else:
                res += [str(i)]
                
        return res