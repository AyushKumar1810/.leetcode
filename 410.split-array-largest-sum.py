#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#

# @lc code=start
class Solution:
    def splitArray(self, nums , k  ):
        # Helper function to check if it is possible to split the array into subarrays with a maximum sum
        def canSplit(largest_sum):
            subarray_count = 0  # Number of subarrays
            current_sum = 0  # Current sum of elements in the subarray

            for num in nums:
                current_sum += num

                # If the current sum exceeds the largest sum allowed, we start a new subarray
                if current_sum > largest_sum:
                    subarray_count += 1
                    current_sum = num

            # After iterating through all elements, check if the number of subarrays is less than or equal to m
            return subarray_count + 1 <= k

        # Determine the range of possible largest sums
        left = max(nums)  # Minimum possible largest sum
        right = sum(nums)  # Maximum possible largest sum

        result = right  # Default result is the maximum possible largest sum

        # Perform binary search to find the minimum largest sum
        while left <= right:
            mid = (left + right) // 2  # Calculate the middle value

            if canSplit(mid):
                # If it is possible to split the array with a maximum sum of mid, update the result
                result = mid
                right = mid - 1  # Narrow down the search range by updating right
            else:
                left = mid + 1  # Adjust the search range by updating left

        return result  # Return the minimum largest sum


        
# @lc code=end

