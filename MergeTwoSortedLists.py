# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#MergeSort
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return []
        head = ListNode(0)
        l3 = head
        while l1 and l2:
            if l1.val < l2.val:
                l3.val = l1.val
                l3.next = ListNode(0)
                l3 = l3.next
                l1 = l1.next
            else:
                l3.val = l2.val
                l3.next = ListNode(0)
                l3 = l3.next
                l2 = l2.next
        if l1:
            l3.val = l1.val
            l3.next = l1.next
        elif l2:
            l3.val = l2.val
            l3.next = l2.next
        return head