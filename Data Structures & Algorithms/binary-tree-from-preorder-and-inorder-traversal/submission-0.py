# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # first item in preorder is the root node
        # use that to "split" the two sides of tree in inorder when building
        # map to find indexes faster with inorder
        inorder_map = {element: index for index, element in enumerate(inorder)}
        preorder_index = 0

        def build(left:int, right:int) -> Optional[TreeNode]:
            # so that preorder idx is still a global var
            nonlocal preorder_index
            if left > right:
                return None

            # create the node with value
            val = preorder[preorder_index]
            preorder_index +=1
            root = TreeNode(val)
            # find that node in inorder to get its children
            mid = inorder_map[val]

            root.left = build(left, mid - 1)
            root.right = build(mid+1, right)
            return root

        return build(0, len(inorder) - 1)
