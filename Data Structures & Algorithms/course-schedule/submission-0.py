class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Creating hash map: for each number up to numCourses starting at 0 with an empty array as the value 
        preMap = { i:[] for i in range(numCourses)}
        # Mapping course number to prereq 
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Creating a set to track the courses we have visited so we don't end up in a infinite loop when performing the DFS. If there is a cycle we have to return False. 
        visitSet = set()

        # We perform a DFS by getting the list of prereqs from the hashmap and performing a further dfs on them until we get a course without requirements meaning we can take it. 
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True 
            # We add the current course to visited to show we have seen it 
            visitSet.add(crs)
            # for each prereq we in the current courses prereq list 
            for pre in preMap[crs]:
                # If the dfs on the prereq returns false we can return false for the entire dfs
                if not dfs(pre): return False
            # If there is a valid pathway for us to take this course then we have to remove it from the set so it doesn't interfere with other course's DFS
            visitSet.remove(crs)
            # Then we mark the list as empty so it can return true and we don't do double work
            preMap[crs] = []
            return True 
        # Now for every coruse we want to perform DFS 
        for crs in range(numCourses):
            if not dfs(crs): return False 
        return True 