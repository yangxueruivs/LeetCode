# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        if not root:
            return False
        if root.val == sum and not root.left and not root.right:
            return True
        
        sum -= root.val
        
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
        