# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        fast = head
        count = 0
        dummy = ListNode(0, head)
        slow = dummy

        # bring fast pointer n steps ahead
        for i in range(n):
            if fast:
                fast=fast.next
            else:
                # just in case
                return head

        #move both pointers until fast reaches end
        slow = dummy
        while fast:
            fast = fast.next
            slow = slow.next

        # slow.next is the node to remove
        slow.next = slow.next.next
        return dummy.next



