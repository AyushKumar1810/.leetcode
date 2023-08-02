#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
#The condition token.isdigit() checks if the token is composed 
# entirely of digits. If it is, it means that the token is a
#  positive number.
#The second part of the condition
#  (token[0] == '-' and token[1:].isdigit()) checks if the 
# token starts with a minus sign ('-') and the remaining characters
#  (token[1:]) are all digits. If this condition is true, it means
#  that the token represents a negative number.
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()
                if token == '+':
                    stack.append(left + right)
                elif token == '-':
                    stack.append(left - right)
                elif token == '*':
                    stack.append(left * right)
                else:
                    stack.append(int(left / right))
        return stack.pop()
            
            
            
            
            
            
            
           



        
# @lc code=end

