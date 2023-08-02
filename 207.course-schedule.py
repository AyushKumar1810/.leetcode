#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start

#NOTE: we can make a graph based onour question abd we have to take care of following things:
#1. If we are getting a loop then return False i.e If course in visitset ( means we are visting course twice {Loop formed})  ... 
#2. If prerequisites [course] ==[] (means the node is no children ) retun True 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
            # Convert the prerequisites list to an adjacency list representation of the graph

        graph={i:[] for i in range(numCourses)}
        for course , prereq in prerequisites :
            graph[course].append(prereq)
        def has_cycle(course,visited):
        # If the course is currently being visited (in the current DFS traversal), there's a cycle

            if visited[course]==1:
                return True
            if visited[course]==2:
            # If the course has already been visited and DFS traversal is complete, no cycle

                return False
         # Mark the course as being visited in the current DFS traversal

            visited[course]=1
        # Explore all the neighbors (prerequisites) of the current course

            for neighbor in graph[course]:
                if has_cycle(neighbor,visited):
                    return True
            # Mark the course as visited (DFS traversal complete)

            visited[course]=2
            return False
    # Perform DFS for each course to check for cycles

        visited=[0]*numCourses # we are visiting each course
        for course  in range(numCourses):
            if has_cycle(course,visited):
                return False
    # If no cycle is found, all courses can be completed (topological sort is possible)

        return True
    



        
# @lc code=end

