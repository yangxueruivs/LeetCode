# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#Double pointer
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head.next:
            return []
        start, end, temp, flag = head, head, head, True
        for i in range(n-1):
            end = end.next
        while end.next:
            flag = False
            temp = start
            start = start.next
            end = end.next
        if flag:
            return head.next
        temp.next = start.next
        return head