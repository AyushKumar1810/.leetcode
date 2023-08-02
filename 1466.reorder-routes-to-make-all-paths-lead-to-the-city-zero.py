#
# @lc app=leetcode id=1466 lang=python3
#
# [1466] Reorder Routes to Make All Paths Lead to the City Zero
#

# @lc code=start

import collections

class Solution:
    # def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
    # # Create a graph dictionary to represent the directed graph
    #     graph = {i: [] for i in range(n)}
    
    # # Set to store reversed connections
    #     reversed_connections = set()
    
    # # Variable to keep track of the minimum number of connections to be reversed
    #     count = 0

    # # Create the graph with connections in both directions
    #     for a, b in connections:
    #     # Connection from city a to city b with direction 1 (forward)
    #         graph[a].append((b, 1))
        
    #     # Connection from city b to city a with direction 0 (reverse)
    #         graph[b].append((a, 0))
        
    #     # Store the reversed connection (b, a) in the set
    #         reversed_connections.add((b, a))

    # # Define a DFS function to traverse the graph and calculate the count
    #     def dfs(node):
    #         nonlocal count
        
    #     # Iterate through neighbors of the current city
    #         for neighbor, direction in graph[node]:
    #         # Check if the connection (node, neighbor) needs to be reversed
    #             if (node, neighbor) not in reversed_connections:
    #             # Increment the count if the connection is not reversed
    #                 count += direction
                
    #             # Continue the DFS from the neighbor
    #                 dfs(neighbor)

    # # Start the DFS from city 0
    #     dfs(0)

    # # Return the minimum number of connections to be reversed
    #     return count

    def minReorder(self,n: int, connections: List[List[int]]) -> int:
    # Step 1: Create sets to store original edges and reversed edges
        original_edges = {(a, b) for a, b in connections}
        reversed_edges = {(b, a) for a, b in connections}
    
    # Step 2: Create dictionaries to represent the directed graph and store neighbors of each city
        graph = {i: [] for i in range(n)}
    
    # Step 3: Populate the graph with connections in both directions
        for a, b in connections:
            graph[a].append(b)  # Forward connection from city 'a' to city 'b'
            graph[b].append(a)  # Reverse connection from city 'b' to city 'a'
    
    # Step 4: Initialize variables for BFS
        visited = set()  # Set to keep track of visited cities
        changes = 0      # Variable to keep track of the number of connections to be reversed
    
    # Step 5: Perform BFS starting from city 0
        queue = collections.deque([0])  # Start BFS from city 0
        visited.add(0)  # Mark city 0 as visited
    
        while queue:
            city = queue.popleft()  # Dequeue a city from the front of the queue
        
        # Traverse the neighbors of the current city
            for neighbor in graph[city]:
                if neighbor in visited:
                    continue  # If the neighbor is already visited, skip to the next neighbor
            
            # Check if the connection (city, neighbor) needs to be reversed
                if (city, neighbor) in original_edges:
                    changes += 1  # Increment the changes count if the connection is forward
                elif (city, neighbor) in reversed_edges:
                # If the connection is already reversed, add it to original_edges and reversed_edges
                    original_edges.add((city, neighbor))
                    reversed_edges.remove((city, neighbor))
                
                queue.append(neighbor)  # Enqueue the neighbor city
                visited.add(neighbor)  # Mark the neighbor city as visited
    
        return changes  # Return the minimum number of connections to be reversed

        
# @lc code=end

