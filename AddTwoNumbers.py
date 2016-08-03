#LinkedList
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        result = res
        carry = 0
        while l1 != None or l2 != None:
            if l1 == None:
                a = 0
                b = l2.val
            elif l2 == None:
                a = l1.val
                b = 0
            else:
                a = l1.val
                b = l2.val
            temp = a + b + carry
            if temp > 9:
                temp %= 10
                carry = 1
            else:
                carry = 0
            res.next = ListNode(temp)
            res = res.next
            if l1:
                l1 = l1.next != None and l1.next or None
            if l2:
                l2 = l2.next != None and l2.next or None
        if carry == 1:
            res.next = ListNode(1)
        return result.next