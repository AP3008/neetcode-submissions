class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # IDEA: This answer uses topological sort but doesn't keep track in the same way as other implementations of the algo. We want to perform a DFS on each course as we come by it until we find a course with no prerequisites, which at that point we append it to our output list. If we detect a cycle in the graph we then return an empty array because it is impossible. We keep track of nodes that have been visited and a set of courses in the current cycle to avoid double work. 
        # Create an adjacency list 
        prereq = { c:[] for c in range(numCourses) }
        for crs, pre in prerequisites: 
            prereq[crs].append(pre)
        
        # A course can have 3 possible states:
            # visited: crs has been added to the output
            # visiting: crs not added to output but added to the cycle 
            # unvisite: crs is not in the output or cycle 

        # Output list 
        output = []
        # Cycle keeps track of the courses visited in search of a class with no prereq's. If we detect a repeated course during this search we need to exit and return an empty list 
        # visit keeps track of all visited sets, if a set has been visited that means that we have seen it before and don't need to continue the DFS to avoid repeated work. 
        visit, cycle = set(), set()
        # DFS function going further into the adjacency list in search of class with no prereq's then adds them to the list.
        def dfs(crs):
            # If there is a cycle detected then we need to return False and immediatley return an empty list. 
            if crs in cycle:
                return False
            
            # If the node has been visited and no cycle has been detected we can conclude that it is fine to continue so we return True 
            if crs in visit:
                return True
            
            # While we are exploring we need to add the course to the set to make sure that we don't find a cycle during the DFS from this course.  
            cycle.add(crs)
            # We loop through all of the edges for this course 
            for pre in prereq[crs]:
                # If any of the further DFS's return False, i.e a cycle was detected, we need to return False until we reach the initial DFS call where we can return the empty list. 
                if not dfs(pre):
                    return False
            # if we looped through and all further DFS calls returned True it means that there is a list of courses we can take as prereqs for the current course we are on. So we can remove this course from the cycle as it hasn't looped. 
            cycle.remove(crs)
            # We add it to the visited set because it is valid and added to the output, so we don't have to take the course again and can avoid double work. 
            visit.add(crs)
            # Adding the course to the output 
            output.append(crs)
            # Returning true because this course is valid if it hasn't failed any of the previous conditions. 
            return True 
        
        # Looping through all of the courses in teh adjacency list. 
        for crs in range(numCourses):
            # If it returns false a cycle has been detected and we return an empty list
            if dfs(crs) == False:
                return []
        # If we make it here, the DFS has build the output. 
        return output