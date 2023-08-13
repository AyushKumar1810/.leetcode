#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start

#NOTE=Here's the intuition that helped me understand this. In this problem, we are searching for the "correct partition" in an array, such that,
# 1. Number of elements in the merged array is (m+n) // 2
# 2. All the elements in the left partition of both the arrays are lesser than or equal to all the elements in the right partition of both the arrays
# 3. If ALeft > BRight --- shrink the partition
# 4. If BLeft > ARight --- increase the partition

# How do we know we can apply Binary search?
# - We have a rule which can tell us if we should move to the right or to the left in the solution space

# Here binary search can be run on any of the arrays, but we choose to run on the smaller one as it's more efficient.


# with use of inbuilt python function 
# class Solution:
    # # def findMedianSortedArrays(self, nums1, nums2) -> float:
    # #     merged = sorted(nums1 + nums2)
    # #     length = len(merged)
    # #     if length % 2 == 0:
    # #         return (merged[length // 2 - 1] + merged[length // 2]) / 2
    # #     else:
    # #         return merged[length // 2]
# Very complex solution :
class Solution:
    def findMedianSortedArrays(self, nums1,nums2):
        if len(nums1) > len(nums2):
            # Make sure nums1 is always the smaller length array
            return self.findMedian(nums2, nums1)
        return self.findMedian(nums1, nums2)

    def findMedian(self, A,B):
        total = len(A) + len(B)
        half = total // 2

        left, right = 0, len(A) - 1

        while True:
            # Binary search to find the split point in array A
            splitA = (left + right) // 2
            splitB = half - (splitA + 1) - 1  # adjusted as per 0 indexing

            # Determine the elements around the split points
            Aleft = float('-inf') if splitA < 0 else A[splitA]
            Aright = float('inf') if splitA + 1 >= len(A) else A[splitA + 1]
            Bleft = float('-inf') if splitB < 0 else B[splitB]
            Bright = float('inf') if splitB + 1 >= len(B) else B[splitB + 1]

            if Aleft <= Bright and Bleft <= Aright:
                # Found the correct split, determine the median
                if total % 2 == 1:  # odd number of elements
                    return float(min(Aright, Bright))
                else:  # even number of elements
                    return float((max(Aleft, Bleft) + min(Aright, Bright)) / 2)
            elif Aleft > Bright:
                # Adjust the split point in array A to the left
                right = splitA - 1
            else:
                # Adjust the split point in array A to the right
                left = splitA + 1

    
        
# @lc code=end

