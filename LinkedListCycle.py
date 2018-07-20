# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        p1, p2 = head, head
        if not p2.next or not p2.next.next:
            return False
        p1 = p1.next
        p2 = p2.next.next
        while p1 != p2:
            if not p2 or not p2.next or not p2.next.next:
                return False
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True
        return True