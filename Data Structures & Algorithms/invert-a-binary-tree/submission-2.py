# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # IDEA: Have a base case checking if the root is null, if it is we return None, otherwise we simply perform the invertTree fucntion again on the left and right nodes, and then switch the left with the right node. 

        if not root: return None
        l = self.invertTree(root.left)
        r = self.invertTree(root.right)
        root.left, root.right = r,l 
        return root 