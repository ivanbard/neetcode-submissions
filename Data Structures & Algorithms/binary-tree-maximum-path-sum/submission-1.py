# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            if root is None:
                return 0

            nonlocal max_path_sum
            # max of child vs 0 to throw away negative subtree
            left_sum = max(dfs(root.left), 0) 
            right_sum = max(dfs(root.right), 0) 

            curr_sum = root.val + left_sum +right_sum

            max_path_sum = max(curr_sum, max_path_sum)
            # not returning actual max path as its a global var
            # and we also return current node + its highest val child to continue exploration
            return root.val+max(left_sum, right_sum)

        # initialize to negative inf because negatives are allowed in tree
        max_path_sum = float('-inf')
        dfs(root)
        return max_path_sum