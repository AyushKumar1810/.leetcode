#
# @lc app=leetcode id=1209 lang=python3
#
# [1209] Remove All Adjacent Duplicates in String II
#

# @lc code=start

#The basic conditions we have is that when we encounter a character we append to 
# the stack and also maintaning it's count to 1 if it's a then [a,1 ] is appended 
# if again a the [a,2] is appended here we are increasing count by 1 if we are 
# getting same char , else : we are just appending char with count 1 i.e [char ,1 ] .
# and the last condition as we have given K so it count reaches == 3 then we are 
# popping it out . and last we are returning our result .
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])
        
        result = ""
        for char, count in stack:
            result += char * count
        
        return result

        
# @lc code=end

