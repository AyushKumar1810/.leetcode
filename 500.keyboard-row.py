#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#

# @lc code=start
# class Solution:
#     def findWords(self, words: List[str]) -> List[str]:
#         keyboard = [ set("qwertyuiop"), set("asdfghjkl"), set("zxcvbn m") ]# space is included in the last row of the keyboard 
#         result = []
#         for word in words: # iterate through each word in the list of words 
#             for row in keyboard: # iterate through each row in the keyboard 
#                 if set(word.lower()).issubset(row): # convert to lowercase to avoid case sensitivity 
#                     result.append(word)
#                     break
#                 return result
# its wrong because the return statement is inside the for loop, so it will return the result after the first iteration. 
class Solution: 
    def findWords(self, words: List[str]) -> List[str]:
        keyboard = [ set("qwertyuiop"), set("asdfghjkl"), set(" zxcvbnm") ] # space is included in the last row of the keyboard
        result = [] 
        for word in words:
            for row in keyboard:
                if set(word.lower()).issubset(row): # convert to lowercase to avoid case sensitivity 
                    result.append(word)
                    break
        return result
# this is the correct implementation of the code.
# time complexity is O(n*m) where n is the number of words and m is the number of characters in each word.
# space complexity is O(1) because the keyboard is a constant size.



# @lc code=end

