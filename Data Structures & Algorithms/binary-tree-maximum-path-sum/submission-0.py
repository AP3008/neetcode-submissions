# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # IDEA: 
        
        # Using a global variables to keep track of the maximum element, if we weren't to do this, we would return two values and take in two arguments for the dfs
        res = [root.val]

        # Max path without splitting
        def dfs(root):
            # If the root we take in is empty we cannot include its value so we return 0 
            if not root:
                return 0 

            # We want to take the max of the left and right subtrees so we recursiveley try and get the max from the left and right side without splitting to add them up as a path.
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            # If the max from the left side and right side return a negative number we just set it to zero and don't include the subtree in our calculation. 
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # We want to check if the sum of this entire tree is greater than the current greatest path. If it is, we change the result variable.
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # Since we are not including the split we want to take the max "choice" or side to go down and include that in the path. 
            return root.val + max(leftMax, rightMax)
        # We run the dfs on the root 
        dfs(root)
        # return the greatest path that we have seen. 
        return res[0]