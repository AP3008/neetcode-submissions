# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
       # IDEA: similar to isSameTree except we want to check if at every subtree is it the same tree. So we perfrom a DFS on the left and right children to see if they are the same tree. 
        if not subRoot: return True 
        if not root: return False 

        def dfs(p, q):
            if not p and not q:
                return True 
            if (not p and q or 
                p and not q or
                p.val != q.val):
                return False
            return dfs(p.left, q.left) and dfs(p.right, q.right)
        
        if dfs(root, subRoot): return True
        l = self.isSubtree(root.left, subRoot)
        r = self.isSubtree(root.right, subRoot)
        return l or r
     