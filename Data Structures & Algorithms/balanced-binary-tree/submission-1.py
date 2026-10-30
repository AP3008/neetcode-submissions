# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # IDEA: Get height of the subtrees and check if it is within one of each other. perform dfs and call isBalanced on both left and right trees

        def dfs(node):
            if not node: return [True, 0]
            l = dfs(node.left)
            r = dfs(node.right)
            flag = False 
            if abs(l[1]-r[1])<= 1 and l[0] and r[0]:
                flag = not flag
            return [flag, 1 + max(l[1],r[1])]
        
        return dfs(root)[0]