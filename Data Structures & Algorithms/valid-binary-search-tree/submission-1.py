# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # IDEA: Because we need to check if the entire right side and left side is within bounds we create a helped dfs function that lets keep track of the bounds as we go down the tree. 

        def valid(node, left, right):
            if not node:
                # Empty binary search tree is a valid BST 
                return True
            # If node.val is not between the right and left bounds then we don't have a valid BST 
            if not (node.val < right and node.val > left):
                return False
            # For the left node we check if it is within the previous left bounds and the current value for node.val 
            # For the right side we make sure that it is greater than the current value of node.val and within the right bounds. 
            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))
        return valid(root, float('-inf'), float('inf'))