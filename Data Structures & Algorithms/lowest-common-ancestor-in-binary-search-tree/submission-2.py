# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # given 2 nodes, find lowest node that is a parent of both
        # binary search tree!! left node is less than current node for all nodes
        # maintain lowest node up until reaching p and q split
        current = root
        if current.val == p.val or current.val == q.val:
            return current

        # traverse to node they split at
        # if both targets smaller, move left
        if current.val >= p.val and current.val >= q.val:
            return self.lowestCommonAncestor(current.left, p, q)
        elif current.val < p.val and current.val < q.val:
            return self.lowestCommonAncestor(current.right, p, q)
        else: 
            return current