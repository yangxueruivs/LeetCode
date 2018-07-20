class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        if not nums1 or not nums2:
            return res
        
        i, j = 0, 0
        nums1.sort()
        nums2.sort()
        while i < len(nums1) and j < len(nums2):
            #print(len(nums1), i, len(nums2), j)
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res += [nums1[i]]
                i += 1
                j += 1
        
        return res