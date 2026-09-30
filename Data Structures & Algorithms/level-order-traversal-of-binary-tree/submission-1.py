# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # return nested list with each list being nodes at the tree level
        if root == None:
            return []
        trav = []
        queue = collections.deque([root])

        while queue:
            # list to store nodes on one level
            lev = []
            for _ in range(len(queue)):
                node = queue.popleft()
                lev.append(node.val)

                # if right and/or left child exist add them next to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # store levels traversal result to final list
            trav.append(lev)

        return trav