# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # IDEA: To get the kth smallest element we just need to do an inorder traversal left -> root -> right, and then we pop off k elements 

        if not root: return 0
        n = 0
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left 
            # curr becomes null so we need to pop the most recent element of the stack 
            curr = stack.pop()
            n+=1
            if n == k:
                return curr.val 
            curr = curr.right
        return -1
        
