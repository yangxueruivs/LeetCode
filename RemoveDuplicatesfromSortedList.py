# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        x = head
        while x.next:
            if x.val == x.next.val:
                x.next = x.next.next
            else:
                x = x.next
            if not x:
                break
        return head