#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
# 1st way to solve the problem   using XOR operator 
class Solution:
    def singleNumber(self, nums):
        res=0
        for n in nums:
            res=n^res
        return res

# 2nd way to solve the problem  uisng set() function 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums) # 2*(a+b+c)-(a+a+b+b+c) = c
         #* example: 2*(1+2+3)-(1+1+2+2+3) = 3  
# 3rd way to solve the problem using Counter() function from collections module 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        return Counter(nums).most_common()[-1][0]
#4th way to solve the problem using dictionary 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d.pop(i)
            else:
                d[i] = 1
        return d.popitem()[0]
# 5th way to solve the problem using list comprehension 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return [x for x in nums if nums.count(x) == 1][0]

# @lc code=end

