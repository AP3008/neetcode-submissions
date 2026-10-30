# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS and use a queue for this one.
        # append a list of values to a result list for each layer of exploration.
        if not root: return []  
        q = deque() 
        res = list()
        q.append(root)
        while q:
            layer = []
            for i in range(len(q)):
                curr = q.popleft()
                layer.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(layer)
        return res 
         