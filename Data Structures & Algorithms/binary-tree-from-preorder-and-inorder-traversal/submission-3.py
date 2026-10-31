# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # If given preorder we know it follows root -> left -> right, and inorder follows left -> root -> right. Since the root is added first in preorder we can use that to build the list and to figure out the nodes that are on the right and left we can find the index of the root and split the inorder list. The leftside of the split corresponds to the left side of the tree and the same for the right hand side. 

        # If the lists are empty we can return nothing
        
        #if not preorder or not inorder:
        #    return None
        
        # We create our root as the root of preorder 
       
        #root = TreeNode(preorder[0])
        
        # We want to find the mid index, which is where the root is in the inorder list. We use the index function in python to locate the value at preorder[0] (the root) and grab its index in the inorder list
        
        #mid = inorder.index(preorder[0])
        
        # we recursively build the tree by setting root.left to the node returned by calling the buildTree function again. For the list we use a sublist of preorder and inorder. The preorder list will be from the first value after the top because that is in the tree already, to mid+1. The inorder list includes everything from the beginning of the list up until mid (the root of the tree exclusive)
        
        #root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        
        # We do the same for the right node but we are starting from mid+1 to the end of the tree because that is where the right side begins. For inorder it is the same since they follow: pre = root -> l -> r, in = l -> root -> r
        
        #root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        # We return the root because at the end we want to return the root of the entire tree, but we also use this node as values for building the tree. 
        
        #return root

        preIdx = inIdx = 0
        def dfs(limit):
            nonlocal preIdx, inIdx
            if preIdx >= len(preorder):
                return None
            if inorder[inIdx] == limit:
                inIdx += 1
                return None

            root = TreeNode(preorder[preIdx])
            preIdx += 1
            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root
        return dfs(float('inf'))