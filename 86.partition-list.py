#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head,x):
        left,right=ListNode() , ListNode()# we are making dummy node
        Ltail,Rtail=left,right
        while head:
# NOTE= so as we have created two node Left , Right if our head value is greater
#  than x then we will put it into left , and if it's greater than x we will put 
# it into right 
            if head.val<x:# Head value less tha x
                Ltail.next=head # again checking for next value if next value
                # after head is less than x oer not
                Ltail=Ltail.next  # ib=ncreamen the value

            else:
                Rtail.next=head
                Rtail=Rtail.next
            head=head.next  
        Ltail.next=right.next # after finifhing loop we have to ,merge left
        # end (Points to Null) with the right head value and make right end value 
        # to Null/None
        Rtail.next=None
        return left.next
# @lc code=end

