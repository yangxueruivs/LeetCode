class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic, res = {}, []
        for i in nums:
            if dic.get(i):
                dic[i] += 1
            else:
                dic[i] = 1
        
        for j in range(k):
            index = max(dic, key = dic.get)
            res += [index]
            dic.pop(index)
            
        return res