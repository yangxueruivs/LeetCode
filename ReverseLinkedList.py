# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []
        
        tail = head
        nextp = head.next

        while nextp:
            prevp = tail
            tail = nextp
            nextp = tail.next
            tail.next = prevp
        head.next = None 
        
        return tail