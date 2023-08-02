#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):


    def addTwoNumbers(self,l1, l2):
    # Create a dummy node to serve as the head of the resulting linked list
        dummy = ListNode()
    # Create a reference to the current node, starting from the dummy node
        cur = dummy
    # Initialize the carry to 0
        carry = 0

    # Traverse both input linked lists until they reach the end and there is no carry left
        while l1 or l2 or carry:
        # Retrieve the values of the current nodes, or 0 if the nodes are None
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

        # Compute the sum of the current digits and the carry
            total = v1 + v2 + carry
        # Update the carry by dividing the total by 10
            carry = total // 10
        # Calculate the value to be stored in the new node
            val = total % 10

        # Create a new node with the calculated value
            cur.next = ListNode(val)
        # Move the current node pointer to the newly created node
            cur = cur.next

        # Move to the next nodes in the input linked lists
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

    # Return the resulting linked list starting from the node after the dummy node
        return dummy.next
       
        
# @lc code=end

