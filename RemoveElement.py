class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        if len(nums) == 0:
            return 0
        while True:
            if i == len(nums)-1:
                #print nums, i
                break
            #print i
            if nums[i] == val:
                nums.remove(val)
            else:
                i += 1
        if nums[-1] == val:
            nums.remove(val)
        return len(nums)