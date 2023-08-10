#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
#NOTE:Approach:
# The steps are as follows:

# First, we will sort the entire array.
# We will use a loop(say i) that will run from 0 to n-1. This i will represent the fixed pointer. In each iteration, this value will be fixed for all different values of the rest of the 2 pointers. Inside the loop, we will first check if the current and the previous element is the same and if it is we will do nothing and continue to the next value of i.
# After that, there will be 2 moving pointers i.e. j(starts from i+1) and k(starts from the last index). The pointer j will move forward and the pointer k will move backward until they cross each other while the value of i will be fixed.
# Now we will check the sum i.e. arr[i]+arr[j]+arr[k].
# If the sum is greater, then we need lesser elements and so we will decrease the value of k(i.e. k–). 
# If the sum is lesser than the target, we need a bigger value and so we will increase the value of j (i.e. j++). 
# If the sum is equal to the target, we will simply insert the triplet i.e. arr[i], arr[j], arr[k] into our answer and move the pointers j and k skipping the duplicate elements(i.e. by checking the adjacent elements while moving the pointers).
# Finally, we will have a list of unique triplets.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array in ascending order
        triplets = []  # Initialize an empty list to store triplets

    # Iterate through each index up to the third-to-last index
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate elements for the current i

        # Initialize pointers left and right
            left, right = i + 1, len(nums) - 1
            target = -nums[i]  # Calculate the target value for the triplet sum

        # While left pointer is less than right pointer
            while left < right:
                if nums[left] + nums[right] == target:
                # If sum of left and right values equals target
                    triplets.append([nums[i], nums[left], nums[right]])  # Add triplet to the list

                # Skip duplicates by incrementing left and decrementing right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1  # Increment left pointer if sum is less than target
                else:
                    right -= 1  # Decrement right pointer if sum is greater than target

        return triplets  # Return the list of triplets

# Example usage
# nums = [-1, 0, 1, 2, -1, -4]
# result = threeSum(nums)
# print(result)  # Output: [[-1, -1, 2], [-1, 0, 1]]


        
# @lc code=end

