# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
       # IDEA: find the node if it exists, if it doens't we just return the root. 
       # If we delete a node we need to put the largest node on the left subtree or smallest node on the right subtree, and call delete node recursively to get rid of the duplicate value. 
       # If the root is null we return the root 
        if not root: return root

        # If the key is greater than the current node we want to explore down the right side 
        if key > root.val:
            # So we recursiveley call deleteNode so we can set the root.right to whatever node gets returned from this recursive call
            root.right = self.deleteNode(root.right, key)
        # We explore the left subtree if the key is smaller 
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # If we have found the key we enter this branch 
        else:
            # If the right root is empty and the node to delete we return the right node 
            if not root.left:
                return root.right 
            # If the right node is empty we return the left node and its subtree 
            elif not root.right:
                return root.left 
            # If we have both children we want to look for the smallest value in the right subtree to replace our current node. 
            #Find the min from right subtree
            # We set our current node to the root of the right subtree
            cur = root.right
            # Then we search for the smallest value in the right subtree which can be done by just exploring left until we hit a null element. 
            while cur.left:
                cur = cur.left 
            # then we set the current root.val to the smallest element in the right subtree, because on this iteration root.val is the node to be replaced so we now want to replace it with the value stored in cur.val. 
            root.val = cur.val 
            # Since the tree now has duplicates of cur.val, we need to replace that original smallest node in the right subtree, so we use cur.val or root.val (they are the same value) as the key that we want to delete, and use the right subtree as the root, and replace our root.right with the recurisve call of deleteNode. 
            root.right = self.deleteNode(root.right, root.val)
        return root 