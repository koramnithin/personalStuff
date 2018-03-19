# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # res = ListNode()
        head = res = None
        if not res:
            if l1.val > l2.val:
                head = res = ListNode(l2.val)
            else:
                head = res = ListNode(l1.val)
        while l1 and l2:
            if l1.val > l2.val:
                res.next = ListNode(l2.val)
                l2 = l2.next
            elif l1.val <= l2.val:
                res.next = ListNode(l1.val)
                l1 = l1.next
            res = res.next
        if l1 and not l2:
            while l1:
                res = ListNode(l1.val)
                res = res.next
                l1 = l1.next
        if l2 and not l1:
            while l1:
                res = ListNode(l2.val)
                res = res.next
                l2 = l2.next
        return head.next

l1 = ListNode(1)
l1.next = ListNode(1)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(5)
l2 = ListNode(2)
l2.next = ListNode(2)
l2.next.next = ListNode(4)
s = Solution()
s.mergeTwoLists(l1,l2)

