# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # how do i track if its coming from left or right?
        # assume no duplicates?

        def dfs(root, low, high):
            if root is None:
                return True

            # if current val is not b/w high and low its not a BST
            if not low < root.val < high:
                return False

            return (dfs(root.left, low, root.val) and dfs(root.right, root.val, high))

        # start with -inf and inf so nodes in tree can compare
        return dfs(root, float("-inf"), float("inf"))