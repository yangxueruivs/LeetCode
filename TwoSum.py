#HashTable
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashTable = {}
        index = 0
        for i in range(len(nums)):
            hashTable[nums[i]] = i
        for j in range(len(nums)):
            temp = target - nums[j]
            if hashTable.has_key(temp) and hashTable[temp] != j:
                index = hashTable[temp]
                break
        res = [j, index]
        return res