#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums):
#NOTE:This problem is a variation of the popular Dutch National flag algorithm. 

# This algorithm contains 3 pointers i.e. low, mid, and high, and 3 main rules.  The rules are the following:

# arr[0….low-1] contains 0. [Extreme left part]
# arr[low….mid-1] contains 1.
# arr[high+1….n-1] contains 2. [Extreme right part], n = size of the array
# The middle part i.e. arr[mid….high] is the unsorted segment. So, hypothetically the array with different markers will..
#So we only have to make arr[mid….high]  sorted and For that we have The steps will be the following:

# First, we will run a loop that will continue until mid <= high.
# There can be three different values of mid pointer i.e. arr[mid]
# If arr[mid] == 0, we will swap arr[low] and arr[mid] and will increment both low and mid. Now the subarray from index 0 to (low-1) only contains 0.
# If arr[mid] == 1, we will just increment the mid pointer and then the index (mid-1) will point to 1 as it should according to the rules.
# If arr[mid] == 2, we will swap arr[mid] and arr[high] and will decrement high. Now the subarray from index high+1 to (n-1) only contains 2.
# In this step, we will do nothing to the mid-pointer as even after swapping, the subarray from mid to high(after decrementing high) might be unsorted. So, we will check the value of mid again in the next iteration.
# Finally, our array should be sorted.
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low] # we will shift 0 to the 1 number ( 1st one place {just after low}) 
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

# Example usage:
    # if __name__ == "__main__":
    #     nums = [2, 0, 2, 1, 1, 0]
    #     self.sortColors(nums)
    #     print("Sorted Colors:", nums)


        
# @lc code=end

