# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # given root, find the depth of the tree (longest path)
        if root == None:
            return 0

        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))