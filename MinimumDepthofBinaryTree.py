# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import Queue

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth, tag = 0, TreeNode(10000)
        if not root:
            return depth
        
        q = Queue()
        q.put(root)
        q.put(tag)
        depth += 1
        
        while not q.empty():
            x = q.get()
            if not x:
                continue
            if x.val == tag.val:
                depth += 1
                q.put(tag)
                continue
            if not x.left and not x.right:
                return depth
            q.put(x.left)
            q.put(x.right)
            