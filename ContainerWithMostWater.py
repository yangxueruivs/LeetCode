#Greedy
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j, res = 0, len(height)-1, 0
        while j > i:
            area = min(height[i], height[j])*(j-i)
            if area > res:
                res = area
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return res