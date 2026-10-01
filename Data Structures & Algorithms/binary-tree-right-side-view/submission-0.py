# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # return only the nodes that are visible from the right side of the tree
        #visible = []
        #visible.append(root.val) #root is always visible

        # breadth first search
        def levelRec(root, level, res):
            if root is None:
                return None

            if len(res) <= level:
                res.append([])

            res[level].append(root.val)
            levelRec(root.left, level +1, res)
            levelRec(root.right, level+1, res)

        def levelOrder(root):
            res=[]
            levelRec(root, 0, res)
            return res

        res = levelOrder(root)
        # only the right-most node on each level is seen from right
        # so return (in a list) last elem on each level
        return [level[-1] for level in res]