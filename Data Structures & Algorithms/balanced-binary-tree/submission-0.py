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
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def height(node):
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)

            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            
            return 1 + max(left, right)
        
        return height(root) != -1