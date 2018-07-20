# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        
        p, l = head, []
        while p:
            l += [p.val]
            p = p.next
        
        m = l.copy()
        m.reverse()
        return l == m