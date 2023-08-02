#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # Check if the linked list is empty
        if head is None:
            return head
        
        # Create a dictionary to map original nodes to their copies
        mapping = {}
        curr = head
        
        # Create a copy of the head node and add it to the mapping
        mapping[curr] = Node(curr.val)
        
        # Traverse the original linked list
        while curr:
            # Get the copy node corresponding to the current original node
            copy = mapping[curr]
            
            # Check if the current node has a random pointer and if it is not already in the mapping
            if curr.random and curr.random not in mapping:
                # Create a copy of the random node and add it to the mapping
                mapping[curr.random] = Node(curr.random.val)
            
            # Set the random pointer of the copy node to the corresponding copy of the random node
            copy.random = mapping.get(curr.random)
            
            # Check if the current node has a next pointer and if it is not already in the mapping
            if curr.next and curr.next not in mapping:
                # Create a copy of the next node and add it to the mapping
                mapping[curr.next] = Node(curr.next.val)
            
            # Set the next pointer of the copy node to the corresponding copy of the next node
            copy.next = mapping.get(curr.next)
            
            # Move to the next node in the original linked list
            curr = curr.next
        
        # Return the copy of the head node
        return mapping.get(head)

        
# @lc code=end

