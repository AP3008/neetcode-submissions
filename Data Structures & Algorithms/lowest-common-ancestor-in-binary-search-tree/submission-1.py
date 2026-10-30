# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # We are looking for the first node when p is less than the parent node and q is greater than the parent node. Essentially meaning that there is some sort of split. If this is the case you can conclude that it is the lowest common ancestor. 

        # We want to start at the root
        curr = root
        # Loop until we reach the end of the tree, but since q and p are gaurenteed to be in the tree we will return early.  
        while curr:
            # If both go down the right (greater) path, then we set curr to its right child 
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # If both p and q are less than the current node we travel down the left side.
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left 
            # Otherwise we have found the split and return the current value.
            else:
                return curr 