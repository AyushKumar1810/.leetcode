#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start

# NOTE=this below is using inbuilt set function 
# # class Solution:
# #     def findDuplicate(self,nums):
# #         num_set = set()
    
# #         for num in nums:
# #             if num in num_set:
# #                 return num
# #             num_set.add(num)
    
# #         return None

# NOTE=Now using Hash Map
# # # class Solution:

# # #     def findDuplicate(self,nums):
# # #         num_dict = {}
    
# # #         for num in nums:
# # #             if num in num_dict:
# # #                 return num
# # #             num_dict[num] = True
    
# # #         return None

# NOTE=Using Floyd's Cycle Detection { Quite Hard Approach}
class Solution:
    def findDuplicate(self, nums):
        slow = 0
        fast = 0

        # Move the pointers until a cycle is detected
        while True:
            slow = nums[slow]  # Move slow pointer one step
            fast = nums[nums[fast]]  # Move fast pointer two steps

            # Check if the pointers meet, indicating a cycle
            if slow == fast:
                slow = 0  # Reset slow pointer to start of the list

                # Find the entry point of the cycle
                while slow != fast:
                    slow = nums[slow]  # Move slow pointer one step
                    fast = nums[fast]  # Move fast pointer one step

                return slow


# @lc code=end

