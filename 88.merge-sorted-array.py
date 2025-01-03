#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
#NOTE:The steps are as follows:

# We will first declare a third array, arr3[] of size n+m, and two pointers i.e. left and right, one pointing to the first index of arr1[] and the other pointing to the first index of arr2[].
# The two pointers will move like the following:
# If arr1[left] < arr2[right]: We will insert the element arr1[left] into the array and increase the left pointer by 1.
# If arr2[right] < arr1[left]: We will insert the element arr2[right] into the array and increase the right pointer by 1.
# If arr1[left] == arr2[right]: Insert any of the elements and increase that particular pointer by 1.
# If one of the pointers reaches the end, then we will only move the other pointer and insert the rest of the elements of that particular array into the third array i.e. arr3[].
# If we move the pointer like the above, we will get the third array in the sorted order.
# Now, from sorted array arr3[], we will copy first n(size of arr1[]) elements to arr1[], and the next m(size of arr2[]) elements to arr2[].
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
       
    # Create a copy of nums1
        nums1_copy = nums1[:m]

    # Initialize pointers for nums1_copy, nums2, and merged array
        i, j, k = 0, 0, 0

    # Merge nums1_copy and nums2 into nums1
        while i < m and j < n:
            if nums1_copy[i] <= nums2[j]: # If nums1_copy[i] is smaller, append it to nums1 and increment i by 1 
                nums1[k] = nums1_copy[i] # Append nums1_copy[i] to nums1 and increment i by 1 
                i += 1
            else:
                nums1[k] = nums2[j] # Append nums2[j] to nums1 and increment j by 1 
                j += 1 # Increment k by 1 to move to the next position in nums1 
            k += 1  # Increment k by 1 to move to the next position in nums1 
        while i < m: # Append the remaining elements of nums1_copy to nums1 and increment i by 1 
            nums1[k] = nums1_copy[i] # Append the remaining elements of nums1_copy to nums1 and increment i by 1 
            i += 1
            k += 1

        while j < n: # Append the remaining elements of nums2 to nums1 and increment j by 1 
            nums1[k] = nums2[j] # Append the remaining elements of nums2 to nums1 and increment j by 1 
            j += 1
            k += 1



        
# @lc code=end

