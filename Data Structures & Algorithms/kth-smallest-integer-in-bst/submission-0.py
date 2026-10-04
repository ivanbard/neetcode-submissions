# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root):
            nonlocal k
            if root is None:
                return None
            # in order traversal
            # left child -> curr -> right child
            res=dfs(root.left)
            if res is not None:
                return res

            # use k as our count variable
            # reduce it each step, then when 0 were at our kth smallest
            k -= 1
            if k==0:
                return root.val

            return dfs(root.right)

        return dfs(root)