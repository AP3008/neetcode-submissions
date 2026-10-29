class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create an adjacency list 
        prereq = { c:[] for c in range(numCourses) }
        for crs, pre in prerequisites: 
            prereq[crs].append(pre)
        
        # A course can have 3 possible states:
            # visited: crs has been added to the output
            # visiting: crs not added to output but added to the cycle 
            # unvisite: crs is not in the output or cycle 

        output = []
        visit, cycle = set(), set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True 
        
        for crs in range(numCourses):
            # If it returns false a cycle has been detected 
            if dfs(crs) == False:
                return []
        return output