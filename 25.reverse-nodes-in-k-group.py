#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def findLength(self, curr):
        # Function to find the length of the linked list
        l = 0
        while curr:
            l += 1
            curr = curr.next
        return l
    
    def reverseKGroup(self, head,k):
        # Base cases: if head is None, head.next is None, or k is 1, return head as it is
        if head is None or head.next is None or k == 1:
            return head
        
        # Find the length of the linked list
        l = self.findLength(head)
        
        def helper(head, l, k):
            # Recursive helper function to reverse groups of k nodes
            
            # If the length is less than k, no need to reverse, so return head
            if l < k:
                return head
            
            if l >= k:
                count = 0
                temp = head
                prev = next = None
                
                # Reverse the first k nodes in the group
                while count < k:
                    next = temp.next
                    temp.next = prev
                    prev = temp
                    temp = next
                    count += 1
                
                l = l - k
                
                # Connect the reversed group to the remaining reversed groups recursively
                head.next = helper(temp, l, k)
                
                # Return the new head of the reversed group
                return prev
        
        # Call the helper function with the initial head, length, and group size k
        return helper(head, l, k)


        
# @lc code=end

