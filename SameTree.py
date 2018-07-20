# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif (not p or not q) or p.val != q.val:
            return False
        elif not p.left and not p.right and not q.left and not q.right:
            return True
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)