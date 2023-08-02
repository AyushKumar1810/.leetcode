#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start

#NOTE: we are using Dijkstra's algorithm ...
import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)

    # Create the graph from the connections list
        for u, v, w in times:
            graph[u].append((v, w))

    # Initialize the distance array with infinity for all nodes except the source node
        distance = [float('inf')] * (n + 1)
        distance[k] = 0

    # Priority queue to store (distance, node) pairs
        pq = [(0, k)]

        while pq:
            dist, node = heapq.heappop(pq)

        # Skip if the node is already processed with a shorter distance
            if dist > distance[node]:
                continue

        # Update the distances of neighbors
            for neighbor, weight in graph[node]:
                new_distance = dist + weight
                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance
                    heapq.heappush(pq, (new_distance, neighbor))

    # Check if all nodes are reachable from the source and get the maximum distance
        max_distance = max(distance[1:])
        return max_distance if max_distance < float('inf') else -1
        
# @lc code=end

