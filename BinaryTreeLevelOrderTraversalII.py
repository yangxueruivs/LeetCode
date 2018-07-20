# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import Queue

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res, array,flag = [], [], 0
        tag = TreeNode(10000)
        q = Queue()
        q.put(root)
        q.put(tag)
        
        if not root:
            return res
        
        while not q.empty():
            temp = q.get()
            if not temp:
                continue
            if temp.val == tag.val:
                if flag == 1:
                    break
                res.append(array)
                array = []
                q.put(tag)
                flag = 1
                continue
            flag = 0
            array += [temp.val]
            if temp.left:
                q.put(temp.left)
            if temp.right:
                q.put(temp.right)
                
        res.reverse()
        return res