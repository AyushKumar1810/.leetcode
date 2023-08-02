#
# @lc app=leetcode id=739 lang=python
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        #The question is similar to next greater element to the 
        #right and we have to return It's index 
        #so that's why we are taking two input .
        #1 value (tempearature),2 Index of that value(temperature).
        
        n = len(temperatures)
        result = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):#we have traverse from left to right
            while stack and stack[-1][1] <= temperatures[i]:
                stack.pop()
            if stack and stack[-1][1] > temperatures[i]:
                result[i] = stack[-1][0] - i
            stack.append([i, temperatures[i]])
        return result

# @lc code=end

