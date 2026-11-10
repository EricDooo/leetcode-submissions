class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = defaultdict(list)
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        output = []
        visited = set() # To keep track of all courses, break faster
        cycle = set() # Cycles are for each recursion, backtrack by removing

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)

            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs) # If course doesn't have a cycle, add to output
            # In dfs, classes that return first are in order of prereqs, explores chains correctly
            return True


        for crs in range(numCourses): # run dfs on each course for individual islands of courses
            if not dfs(crs):
                return []
        return output