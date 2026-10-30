# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Tracking the longest path 
        self.res = 0

        # we simply perform a dfs to get the height of the tree. 
        def dfs(curr):
            # If the current node is none we return 0 and don't add it to the longest path 
            if not curr: return 0 
            # we perform dfs on both right and left nodes to try and get the height of the subtrees 
            l = dfs(curr.left)
            r = dfs(curr.right)
            # If the height of the left subtree to the height of the right subtree is greater than the current res we replace it as the new lognest path 
            self.res = max(self.res, l + r)
            # We increase by 1 to include the node on the path and take the max of the left and right subtree to get the height.
            return 1 + max(l,r)
        # calling dfs on the root so we can calculate the diameter 
        dfs(root)
        # return the res 
        return self.res 