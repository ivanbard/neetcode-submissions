# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # maintain track of vals of path to node from root
        # path contains no node.vals > current node val = good node
        # path contains node.val >= current node val = bad node
        #good_nodes = 0
        #maximum = 0

        def dfs(node, max_so_far):
            if node is None:
                return 0

            # 1-by-1 node checks
            # returning 1 or 0 based on if curr node is good/bad
            if node.val >= max_so_far:
                good_nodes = 1
            else:
                good_nodes = 0
            next_max = max(max_so_far, node.val)

            # traverse to next nodes in tree
            good_nodes += dfs(node.left, next_max)
            good_nodes += dfs(node.right, next_max)

            return good_nodes

        if root is None:
            return 0

        return dfs(root, root.val) # since root is always good + first max
            