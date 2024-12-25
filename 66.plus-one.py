#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 1. Convert the list of digits to a number
        num = 0
        for i in range(len(digits)): # len(digits) returns the number of elements in the list digits. For example, if digits is [1, 2, 3], then len(digits) is 3.
            num += digits[i] * pow(10, len(digits) - i - 1)# 10**(len(digits) - i - 1) is the same as pow(10, len(digits) - i - 1) . we are converting the list of digits to a number. For example, if digits is [1, 2, 3], then num is 123. 
        # 2. Add 1 to the number and convert it back to a list of digits 
        num += 1 
        # 3. Convert the number back to a list of digits and return it 
        return [int(i) for i in str(num)] 

    
# @lc code=end

# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         for i in range(len(digits) - 1, -1, -1):
#             if digit[i] < 9:
#                 digits[i] += 1
#                 return digits
#             else:
#                 digits[i] = 0
#         return [1] + digits