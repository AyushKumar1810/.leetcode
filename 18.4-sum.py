#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
#NOTE:Approach:

# The steps are as follows:

# First, we will sort the entire array.
# We will use a loop(say i) that will run from 0 to n-1. This i will represent one of the fixed pointers. In each iteration, this value will be fixed for all different values of the rest of the 3 pointers. Inside the loop, we will first check if the current and the previous element is the same and if it is we will do nothing and continue to the next value of i.
# After checking inside the loop, we will introduce another fixed pointer j(runs from i+1 to n-1) using another loop. Inside this second loop, we will again check for duplicate elements and only perform any further operation if the elements are different.
# Inside the second loop, there will be 2 moving pointers i.e. k(starts from j+1) and l(starts from the last index). The pointer k will move forward and the pointer l will move backward until they cross each other while the value of i and j will be fixed.
# Now we will check the sum i.e. nums[i]+nums[j]+nums[k]+nums[l].
# If the sum is greater, then we need lesser elements and so we will decrease the value of l.
# If the sum is lesser than the target, we need a bigger value and so we will increase the value of k. 
# If the sum is equal to the target, we will simply insert the quad i.e. nums[i], nums[j], nums[k], and nums[l] into our answer and move the pointers k and l skipping the duplicate elements(i.e. by checking the adjacent elements while moving the pointers).
# Finally, we will have a list of unique quadruplets.
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    # Sort the input array in ascending order to simplify the process
        nums.sort()
        quadruplets = []

    # Iterate through the array, considering the first element of the quadruplet
        for i in range(len(nums) - 3):
        # Skip duplicates for the first element of the quadruplet
        # We only consider the first occurrence of each unique element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

        # Iterate through the array, considering the second element of the  quadruplet
            for j in range(i + 1, len(nums) - 2):
            # Skip duplicates for the second element of the quadruplet
            # We only consider the first occurrence of each unique element
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

            # Initialize two pointers, left and right, to find the remaining two elements
                left, right = j + 1, len(nums) - 1

            # Use two pointers technique to find the remaining two elements of the quadruplet
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                    # If the current combination sums up to the target,
                    # add it to the quadruplets list
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])

                    # Skip duplicates for the third element of the quadruplet
                    # We only consider the first occurrence of each unique element
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        left += 1

                    # Skip duplicates for the fourth element of the quadruplet
                    # We only consider the first occurrence of each unique element
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        right -= 1

                    elif total < target:
                    # If the sum is less than the target, move the left pointer to increase the sum
                        left += 1
                    else:
                    # If the sum is greater than the target, move the right pointer to decrease the sum
                        right -= 1

        return quadruplets

      


        
# @lc code=end

