# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = res = ListNode()

        while l1 or l2:
            if not l1:
                res.next = l2
                res = res.next
                l2 = l2.next
            elif not l2:
                res.next = l1
                res = res.next
                l1 = l1.next
            elif l1.val <= l2.val:
                res.next = l1
                res = res.next
                l1 = l1.next
            else:
                res.next = l2
                res = res.next
                l2 = l2.next
        
        return head.next