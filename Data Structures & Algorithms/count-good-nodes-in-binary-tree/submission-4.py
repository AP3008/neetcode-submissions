# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Idea: We want to perform a DFS on this tree keeping track of the max node value as we traverse further down so we know what the greatest value is along the path so we can figure out whether a node is good. We only increment res when it's good otherwise the return value stays at zero. The sum being the result. 
        def dfs(node, maxVal):
            # If the node is null we return 0 
            if not node: return 0 
            # If the node is considered good we set res to 1, otherwise 0 
            res = 1 if node.val >= maxVal else 0
            # We check if the current node is the largest in the path 
            maxVal = max(maxVal, node.val)
            # We add the amount of good nodes on the left side to res
            res += dfs(node.left, maxVal)
            # We add the amount of good nodes on the right to res
            res += dfs(node.right, maxVal)
            # return the sum of all good nodes from the left and right + the check 
            return res
        # We want to return the result of the dfs on root.
        return dfs(root, root.val)