# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        encoded_string = ""
        def dfs(root):
            nonlocal encoded_string
            if root is None:
                encoded_string += "n,"
                return
            else:
                encoded_string += f"{root.val}"

            # add separator char to string
            encoded_string += ","
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        # bracket to close off tree once done
        # actually, dont think its needed
        #encoded_string += "]"
        return encoded_string
            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # obtain list of just the nodes
        nodes = data.split(",")
        i = len(nodes)
        count = 0

        def dfs():
            nonlocal count

            if nodes[count] == "n":
                count += 1
                return None

            root = TreeNode(int(nodes[count]))
            count += 1
            root.left = dfs()
            root.right = dfs()

            return root

        return dfs()
