# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Ideas: This has to take into account a couple of things: 
        # If the node is on the far right it can be seen 
        # If there is a right sibling node, the current node cannot be seen
        # If there is a node on the same level and to the right of it, only the right most node can be seen. 
        # Simply get the level order and take the last node in the queue and assuming that we append in the order left first 

        if not root: return []
        q = deque()
        q.append(root)
        res = []
        while q:
            layer = []
            for i in range(len(q)):
                node = q.popleft()
                layer.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(layer[-1])
        return res 
