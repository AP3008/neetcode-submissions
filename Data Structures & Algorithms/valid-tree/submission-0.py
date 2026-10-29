class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Tree definition: 
            # 1. All nodes must be connected 
            # 2. Must have no cycles 
        # If the tree is empty it is still a tree, so we return true 
        if not n:
            return True 
        
        # We create an adjacency list for the undirected graph 
        adj = { i:[] for i in range(n) }
        # each node points back at each other. 
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        # We track the nodes that we have vistied in a visit set. 
        visit = set()

        # DFS on a specific node, keeping track of the node that we are coming from. 
        def dfs(i, prev):
            # If i has been visited we have gotten a cycle. 
            if i in visit:
                return False
            # If we haven't visited the node before we add it to the set. 
            visit.add(i)
            # we check all of the nodes that i is connected to in the list 
            for j in adj[i]:
                # If we come across the node we came from we want to skip it so we don't get a false positive since it would be in our seen set. 
                if j == prev:
                    continue
                # If the node is not the previous one we want to perform DFS on it using the current node as that one's previous node. If it detects a cycle then we return False 
                if not dfs(j, i):
                    return False 
            # If we get through the nodes connections without any cycles we can safetly return True. 
            return True 
        # We perform DFS on the first node and use -1 as the previous becuase it will never a node value. 
        # We also check if the length of the visiting set is equal to the number of nodes to make sure that the graph is all connected. 
        return dfs(0, -1) and n == len(visit)

        
        