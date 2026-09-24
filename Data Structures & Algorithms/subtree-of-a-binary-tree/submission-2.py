# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    hasSub = False 
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # traverse both trees at once, and fail if node not exact same
        if p is None and q is None:
            return True # both absent, so trees match

        if p is None or q is None:
            return False # tree mismatch, return false

        return(p.val == q.val and self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left))
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # traverse root tree until subRoot equiv is found
        # then traverse both root tree + subroot tree to see if they match
        #if subRoot is None: return True
        if root is None: return False

        #compare
        if not self.hasSub:
            self.hasSub = self.isSameTree(root, subRoot)

        #traverse
        self.isSubtree(root.left, subRoot)
        self.isSubtree(root.right, subRoot)

        return self.hasSub