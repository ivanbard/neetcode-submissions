# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = [], []
        curr1 = l1
        curr2 = l2
        sum_val = 0

        while curr1:
            num1.append(curr1.val)
            curr1 = curr1.next
        
        while curr2:
            num2.append(curr2.val)
            curr2 = curr2.next
        
        # num in 0th pos = num * 10^0
        # num in 1st pos = num * 10^1, etc
        for i in range(len(num1)):
            sum_val += (num1[i] * (10**i))
        for i in range(len(num2)):
            sum_val += (num2[i] * (10**i))
        
        digits_list = [int(d) for d in str(sum_val)]

        dummy = ListNode()
        curr = dummy

        for digit in reversed(digits_list):
            curr.next = ListNode(digit)
            curr = curr.next

        return dummy.next