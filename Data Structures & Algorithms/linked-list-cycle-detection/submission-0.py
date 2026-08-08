# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # cycle = any nodes next pointer being a previous node
        # hash table to track seen nodes
        # view what nodes route back to prev node and save in hash map?
        seen = {}
        prev = None
        curr = head

        while curr:
            # save next address for comparisons
            if curr.next in seen:
                return True
            else:
                seen[curr] = curr.next

            prev = curr
            curr = curr.next

        return False