# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first, second = head, head

        for i in range(n):      # move first n steps forwards
            first = first.next
        if not first:
            return head.next

        while first.next:       # move both pointers until first is at end
            first = first.next
            second = second.next
        second.next = second.next.next  # nth from end is second.next
        return head