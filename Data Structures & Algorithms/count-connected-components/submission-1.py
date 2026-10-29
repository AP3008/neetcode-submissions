class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
       # My Sol. Create adjacency list and perform DFS on each node. Have a set that keeps track of the seen nodes and increment the components count by 1 every time we find a node that isn't apart of the seen set. 

       # Also cover edge cases, if n = 0 
        if not n:
            return 0 
        # create adj. list 
        adj = { i:[] for i in range(n) }
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        # set to track what has been seen
        seen = set()
        # To track the number of components 
        components = 0 
        # We perform DFS on all of the nodes, marking all of the nodes that have been seen as apart of the set 
        def dfs(node):
            # If the node has been seen, we don't need to perform DFS on it. So we just return False 
            if node in seen:
                return False
            # We haven't seen it so we add it to the set 
            seen.add(node)
            # Now for each adjacent node we want to perform dfs on it 
            for j in adj[node]:
                dfs(j)
            # We return True so we can continue iterating. 
            return True 
        # We need to go through all of the nodes and all of the nodes that we are allowed to perform a DFS on (they return True) we increment the components. If we cannot increment 
        for v in adj:
            if dfs(v) == False:
                continue 
            components+=1 
        return components


            
