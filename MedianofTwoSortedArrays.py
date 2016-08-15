#Merge sort
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i, j, res, len1, len2 = 0, 0, [], len(nums1), len(nums2)
        while i < len1 and j < len2:
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        while i < len1:
            res.append(nums1[i])
            i += 1
        while j < len2:
            res.append(nums2[j])
            j += 1
        length = len(res)
        if length % 2 == 0:
            return (res[length/2]+res[length/2-1])/2.0
        else:
            return res[length/2]