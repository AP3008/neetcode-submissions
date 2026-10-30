class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Idea: We want to remove an edge from the graph that makes this a valid tree. We are not told the amount of nodes in the graph because if there are n nodes there has to be n - 1 nodes for it to be a tree. 

        # Getting the number of nodes in the list 
        N = len(edges)

        # For each index we want to make a parent list where the parent is itself and the indexes correspond to the node and the value is the parent. 
        par = [ i for i in range(N+1) ]
        # rank list each index is the node and the value is the amount of children nodes it has. 
        rank = [1] * (N+1)

        # Our find function 
        def find(n):
            # When n is not its own parent, we want to keep on searching for it's parent 
            if n != par[n]:
                par[n] = find(par[n])
            
            # return the parent of the node, since parent of n is itself we can just return par[n]
            return par[n]
        
        # Union function 
        def union(n1, n2):
            # We find the parents of n1 and n2 
            p1, p2 = find(n1), find(n2)
            # if both have the same parent we return False 
            if p1 == p2:
                return False
            # If the rank of p1 is greater than the rank of p2 we can set the parent of p2 as p1, creating a union on the graph 
            if rank[p1] > rank[p2]:
                par[p2] = p1
                # We add on the rank of p2 to p1 because it is now the parent
                rank[p1] += rank[p2]
            else:
                # We do the same thing just p2 and p1 are switched. 
                par[p1] = p2
                rank[p2] += rank[p1]
            # Then return true once a union is made
            return True 
        
        # We iterate through the edges and perform a union on all of the edges. 
        for n1, n2 in edges:
            # If we get a false, we got a cycle and we remove this edge. 
            if not union(n1, n2):
                return [n1, n2]