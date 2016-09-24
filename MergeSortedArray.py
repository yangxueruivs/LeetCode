class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i, j, n1, n2 = 0, 0, nums1[:m], nums2[:n]
        while i<len(n1) and j<n:
            if n1[i] < n2[j]:
                i += 1
            else:
                n1.insert(i, n2[j])
                j += 1
                i += 1
        if j<n:
            n1 += n2[j:]
        nums1[:] = n1[:]