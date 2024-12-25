#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start

# solve using hashmap
class Solution:
    def majorityElement(self, nums):
        count={}
        for n in nums :
            count[n]=1 + count.get(n,0)
# for eg : When n = 2 is encountered, count.get(n, 0) returns 0
#  (since n is not present in the dictionary). Therefore, count[2] = 0 + 1 assigns 
# the value 1 to the key 2 in the dictionary.
            if count[n] > len(nums)//2:
                return n

class Solution:
    def majorityElement(self, nums):
        count = {}  # create a dictionary to store the count of each element in the list  
        for n in nums: 
            count[n] = 1 + count.get(n, 0) # get the count of the element n in the dictionary, if it is not present, return 0 and add 1 to it how? count.get(n, 0) returns 0 (since n is not present in the dictionary). Therefore, count[2] = 0 + 1 assigns the value 1 to the key 2 in the dictionary.  
            if count[n] > len(nums) // 2:
                return n



# @lc code=end
