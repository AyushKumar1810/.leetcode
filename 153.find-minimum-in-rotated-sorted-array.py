#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start


#NOTE= Point to be noted here minimum element should or will be definetly in the unsorted array part , so we only have to find unsorted part and find minimum 
class Solution:
    def findMin(self, nums):
        # Initialize the left and right pointers
        left, right = 0, len(nums) - 1

        # Perform binary search until the left pointer becomes greater than or equal to the right pointer
        while left < right:
            # Calculate the middle index
            mid = (left + right) // 2

            # Check if the element at mid+1 is smaller than the element at mid
            if nums[mid+1] < nums[mid]:
                # If true, the element at mid+1 is the minimum, so return it
                return nums[mid+1]

            # Check if the element at mid is greater than the element at left
            if nums[mid] > nums[left]:
                # If true, the left half of the array is sorted in ascending order
                # The minimum element must be in the right half, so update the left pointer
                left = mid + 1
            else:
                # If false, the right half of the array is sorted in ascending order
                # The minimum element can be in the left half or at the mid index
                # Update the right pointer to mid to include the mid index in the search range
                right = mid

        # Return the element at the left pointer, which represents the minimum element
        return nums[left]


        
# @lc code=end

#Beautiful Explanation. I used the same code for the 154. Find Minimum in Rotated Sorted Array II with just one change and it was accepted. 

# Since in 154 problem, there are duplicates as well, I added an extra check in case all elements at start, mid and end are the same. In that case, we just decrement the end pointer by 1. Otherwise, the code remains the same.


# while start <= end:
#             # If the "start" element is smaller than "end"
#             if nums[start] < nums[end]: return min(minimum, nums[start])

#             mid = start + (end - start) // 2

#             # IF this mid value is smaller than previous minimum we found
#             # Then update the minimum
#             minimum = min(minimum, nums[mid])

#             # If start, end and mid are all same e.g. if [3,3,0,3] is the test case
#             # Then, we will simply decrement end pointer
#             if nums[start] == nums[mid] == nums[end]: end -= 1
#             # Otherwise, we check
#             # Is this "mid" value part of left sorted subarray or right sorted subarray?
#             # If this is part of the left sorted subarray, we will find minimum on right side
#             elif nums[mid] >= nums[start]: start = mid + 1
#             # Otherwise, we will find the minimum on the left side
#             else: end = mid - 1