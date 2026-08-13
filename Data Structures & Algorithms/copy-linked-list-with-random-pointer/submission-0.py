"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        #go through list, note all items in hashmap, then re-create?
        seen = {}
        index_map = {}
        curr = head
        n = 0

        while curr:
            seen[n] = Node(curr.val)
            index_map[curr] = n
            curr = curr.next
            n += 1

        curr = head
        for i in range(len(seen)):
            seen[i].next = seen.get(i + 1)
            seen[i].random = seen[index_map[curr.random]] if curr.random else None
            curr = curr.next

        return seen[0]