#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def findOrder(self,numCourses, prerequisites):
    # Step 1: Convert the prerequisites list to an adjacency list representation of the graph
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[prereq].append(course)

    # Step 2: Define the helper function for DFS traversal with cycle detection
        def dfs(course, visited, order):
            if visited[course] == 1:
            # If the course is currently being visited (in the current DFS traversal), there's a cycle
                return False

            if visited[course] == 2:
            # If the course has already been visited and added to the order, skip it
                return True

        # Mark the course as being visited in the current DFS traversal
            visited[course] = 1

        # Explore all the neighbors (prerequisites) of the current course
            for neighbor in graph[course]:
                if not dfs(neighbor, visited, order):
                    return False

        # Mark the course as visited and add it to the order (topological sort)
            visited[course] = 2
            order.append(course)
            return True

    # Step 3: Perform DFS for each course to find the topological sort order
        visited = [0] * numCourses
        order = []

        for course in range(numCourses):
            if not dfs(course, visited, order):
            # If a cycle is found, it's impossible to finish all courses
                return []

    # Step 4: Reverse the order to get the correct topological sort
        return order[::-1]

# Example usage:
# numCourses = 4
# prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
# result = findOrder(numCourses, prerequisites)
# print(result)  # Output: [0, 2, 1, 3]

        
# @lc code=end

