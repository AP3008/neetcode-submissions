class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Union Find sol. 

        # Idea: Find the amount of unions we can make based of the edges and decrement that from the total number of nodes. 

        # Parent array, that represents each node. So the indexes are the node and the value is the parent of that node. So every node starts as the parent of itself. 
        par = [i for i in range(n)]
        # rank array: Indexes are the specific node and the value is the size of the entire connected component if it was the parent. So all of the nodes "under" it + itself would be the rank of a node. The reason being that we can add new nodes to the larger structure (node with greater rank) because we need to minimize the rank of the tree.
        rank = [1] * n

        # Helper function to help find the parent of a node n1. 
        def find(n1):
            res = n1
            # Loop until res / n1 doesn't have any more parents. 
            while res != par[res]:
                # example of path compression we are setting the parent of res to the grandparent of res. If it doesn't exist this won't do anything, because the nodes parent would be itself, i.e looping over itself making it the same value.  
                par[res] = par[par[res]]
                # setting the parent of n1 as the res, but we are looking for the furthest up parent so until the node is only a parent of itself. 
                res = par[res]
            return res
        
        # Unioning together two nodes that make an edge 
        def union(n1, n2):
            # We want to find the greatest parent of these two nodes 
            p1, p2 = find(n1), find(n2)
            # If they have the same parent, that means that they are already connected and we can return 0 
            if p1 == p2:
                return 0
            
            # If the rank of parent2 is greater than parent1 
            if rank[p2] > rank[p1]:
                # we set the parent of p1 as p2 and increment the rank of p2 by the rank of p1 (if it has any children)
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                # If p1 has a greater rank we do the same thing but for p2 
                par[p2] = p1
                rank[p1] += p2
            # We return 1 because a union operation happened successfully meaning that we want to add 1 to our union count because the number of components are equal to total nodes - unions 
            return 1 
        # storing the amount of components as the number of nodes and decrementing whenever we find a union. 
        res = n 
        # Iterate through all of the edges performing unions on all of the edges. For every valid union that doens't have a shared parent we decrement res so by the end we get (no. nodes - valid unions = components)
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res

