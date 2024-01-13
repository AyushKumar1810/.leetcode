#
# @lc app=leetcode id=863 lang=python3
#
# [863] All Nodes Distance K in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
           
        # Build a graph to represent the connections between nodes
        graph = {}
        self.buildGraph(root, None, graph)

        # Set to keep track of visited nodes
        visited = set()
        # List to store the nodes at distance K from the target
        result = []

        # DFS to find nodes at distance K from the target
        self.dfs(target, k, graph, visited, result)
        return result

    def buildGraph(self, node, parent, graph):
        # Helper function to build the graph using DFS
        if not node:
            return

        if node not in graph:
            graph[node] = set()

        if parent:
            graph[node].add(parent)
            graph[parent].add(node)

        self.buildGraph(node.left, node, graph)
        self.buildGraph(node.right, node, graph)

    def dfs(self, node, k, graph, visited, result):
        # Helper function for DFS traversal
        if not node or node in visited:
            return

        visited.add(node)

        if k == 0:
            result.append(node.val)
            return

        # Recursively explore neighbors at distance K
        for neighbor in graph[node]:
            self.dfs(neighbor, k - 1, graph, visited, result)
        
# @lc code=end

