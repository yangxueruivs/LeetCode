# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        pa, pb = head, head.next
        while pb:
            pa.val, pb.val = pb.val, pa.val
            if not pb.next or not pb.next.next:
                break
            pa = pa.next.next
            pb = pb.next.next
        return head