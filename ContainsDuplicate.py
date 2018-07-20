class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        
        dic = {}
        for i in nums:
            if dic.get(i):
                return True
            else:
                dic[i] = 1
                
        return False