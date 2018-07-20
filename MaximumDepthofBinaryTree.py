# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxD(root):
            if not root:
                return 0
            return max(maxD(root.left)+1, maxD(root.right)+1)
        
        return maxD(root)