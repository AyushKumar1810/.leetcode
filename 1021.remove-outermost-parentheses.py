#
# @lc app=leetcode id=1021 lang=python3
#
# [1021] Remove Outermost Parentheses
#

# @lc code=start
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
#NOTE:In short, the "Remove Outermost Parentheses" problem involves removing the outermost parentheses from every primitive substring within a valid parentheses string. A primitive substring is one that cannot be further split into smaller valid substrings. To solve this problem:

# Initialize an empty result list and an empty stack.

# Iterate through the input string.

# If you encounter an open parenthesis "(", add it to the stack and check if the stack is not empty. If it's not empty, add this parenthesis to the result list.

# If you encounter a close parenthesis ")", pop the corresponding open parenthesis from the stack. If the stack is not empty, add this parenthesis to the result list.

# After processing all characters, join the characters in the result list to form the modified string and return it.

# This solution effectively removes the outermost parentheses from primitive substrings in the input string.
        result=[]
        stack= []
        for char in s :
            if char== "(":
                if stack:
                    result.append(char)
                stack.append(char)
            else:
                stack.pop()
                if stack:
                    result.append(char)
        return "".join(result)
                   
               



# @lc code=end

