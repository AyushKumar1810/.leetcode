#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        # Calculate the effective rotation (handles cases where k > n)

        k=k%n
        # Perform the rotation in-place using slicing and concatenation

        nums[:] = nums[-k:] + nums[:-k]
# @lc code=end

