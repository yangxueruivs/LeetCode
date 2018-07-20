# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        def isSym(left, right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            elif left.val == right.val:
                return isSym(left.left, right.right) and isSym(left.right, right.left)
            else:
                return False
            
        return isSym(root.left, root.right)