# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # iterate to k-th element, reverse that, then move to k+kth element
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        #n = 0

        while True:
            # get to the group boundary
            kth = group_prev.next
            for _ in range(k):
                if kth is None:
                    return dummy.next
                kth = kth.next

            # store "checkpoint" group nodes
            group_start = group_prev.next
            reverse_prev = kth
            current = group_start

            # reverse k-sized node group
            for _ in range(k):
                next_node = current.next
                current.next = reverse_prev
                reverse_prev = current
                current = next_node

            group_prev.next = reverse_prev
            group_prev = group_start