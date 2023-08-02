#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#

# @lc code=start
class Solution:
    def findClosestElements(self, arr,k,x):
        # Define the initial range for the subarray
        start = 0
        end = len(arr) - k

        # Perform binary search within the range
        while start < end:
            # Calculate the middle index of the range
            mid = start + (end - start) // 2

            # Compare the distances between x and the elements at mid and mid + k
            if x - arr[mid] > arr[mid + k] - x:
                # The elements after mid are closer to x
                start = mid + 1
            else:
                # The elements before or at mid are closer to x
                end = mid

        # Return the subarray with the k closest elements
        return arr[start : start + k]


        
# @lc code=end

