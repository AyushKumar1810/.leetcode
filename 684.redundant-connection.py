#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#

# @lc code=start

#NOTE: In this question we have to remove vertices so that given graph becomes tree 
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    # Function to find the parent of a node using Union Find
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
    
    # Function to perform Union of two nodes using Union Find
        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
        
            if root1 == root2:
                return False  # A cycle is detected
            parent[root1] = root2
            return True

    # Create a parent array to keep track of the parent of each node
        parent = [i for i in range(len(edges) + 1)]
    
    # Iterate through the edges and perform Union
        for edge in edges:
            if not union(edge[0], edge[1]):
                return edge  # Return the redundant edge if a cycle is detected

# # Example usage:
# edges = [[1, 2], [1, 3], [2, 3]]
# result = findRedundantConnection(edges)
# print(result)  # Output: [2, 3]

        
# @lc code=end

