# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1NextNode = l1.next
        l2NextNode = l2.next
        num1 = str(l1.val)
        num2 = str(l2.val)

        while l1NextNode is not None:
            num1 = str(l1NextNode.val) + num1
            l1NextNode = l1NextNode.next

        while l2NextNode is not None:
            num2 = str(l2NextNode.val) + num2
            l2NextNode = l2NextNode.next

        sum = int(num1) + int(num2)
        # print(int(num1), int(num2), sum)

        sumInitNode = ListNode()
        currNode = sumInitNode
        backwardsSum = str(sum)[::-1]

        for i, digit in enumerate(backwardsSum):
            # print(digit, i)
            if (i != len(backwardsSum) - 1):
                currNode.next = ListNode()

            currNode.val = int(digit)
            currNode = currNode.next

        return sumInitNode
