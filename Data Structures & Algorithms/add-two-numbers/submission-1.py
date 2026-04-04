# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = res = ListNode()

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            total = v1 + v2 + carry
            if total > 9:
                carry = int(str(total)[0])
                total = int(str(total)[1])
            else:
                carry = 0
            
            res.next = ListNode(total)
            res = res.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next