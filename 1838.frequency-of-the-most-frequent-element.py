#
# @lc app=leetcode id=1838 lang=python3
#
# [1838] Frequency of the Most Frequent Element
#

# @lc code=start

#we can solve the question by finding the maximum element in that array and then substractinh with each element that are less than it and then we can we the idea that how many more we are require to get the same as maximum 

#NOTE:The idea is to sort the array first and then use a sliding window to calculate the frequency of the most frequent element for each possible window size. 
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        nums.sort()  # Sort the array in ascending order
        left = 0  # Left pointer for the sliding window
        max_freq = 0  # Initialize the maximum frequency of the most frequent element
        window_sum = 0  # Initialize the sum of elements within the current window

        for right in range(len(nums)):
            window_sum += nums[right]  # Add the element at the right pointer to the window sum

        # Check if the current window is valid (i.e., the difference between the sum of elements
        # in the window and the window size times the element at the right pointer is not greater than k)
            while (right - left + 1) * nums[right] - window_sum > k:
                window_sum -= nums[left]  # Shrink the window from the left side
                left += 1

        # Update the maximum frequency encountered so far
            max_freq = max(max_freq, right - left + 1)

        return max_freq

# Example usage:
# nums = [3, 9, 6]
# k = 2
# result = maxFrequency(nums, k)
# print(result)  # Output: 1


        
# @lc code=end

