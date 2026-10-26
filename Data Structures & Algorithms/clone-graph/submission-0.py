"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # hashmap of old nodes mapped to our new copies of the node
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                # If the node exists in our hashmap we already made it and simply return our already created copy.
                return oldToNew[node]
            # creating our copy of the old node
            copy = Node(node.val)
            # mapping the old node to the copy, so we know it has alreday been created. 
            oldToNew[node] = copy
            # looping through the neighbors of node
            for n in node.neighbors:
                # calling dfs to create a copy and adding it as a node
                copy.neighbors.append(dfs(n))
            # returning the newly made copy, once neighbors are copied
            return copy

        # running dfs on original node, if the node is null we return None
        return dfs(node) if node else None 
            