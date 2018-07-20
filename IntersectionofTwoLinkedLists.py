# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        hA, hB = headA, headB
        if not hA or not hB:
            return None
        
        def tranverse(head):
            count = 1
            while head.next:
                count += 1
                head = head.next
            return count
        
        def findInter(lenA, lenB, headA, headB):
            while lenA > lenB:
                lenA -= 1
                headA = headA.next
                
            while headA != headB:
                headA = headA.next
                headB = headB.next
            return headA
        
        lenA, lenB = tranverse(hA), tranverse(hB)
        if lenA > lenB:
            return findInter(lenA, lenB, hA, hB)
        else:
            return findInter(lenB, lenA, hB, hA)
        