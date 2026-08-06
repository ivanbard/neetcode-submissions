# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # singly linked - one directional
        prev = None
        curr = head

        while curr:
                # keep next nodes address
                next_node = curr.next
                # set the current nodes next to the prev node
                curr.next = prev
                #update prev node to reflect current
                prev = curr
                # move to next node
                curr = next_node

        return prev