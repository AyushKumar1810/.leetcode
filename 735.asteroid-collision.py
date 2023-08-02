#
# @lc app=leetcode id=735 lang=python
#
# [735] Asteroid Collision
#

# @lc code=start
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
# We have three comdition for our problem .1= If stack is empty and asteroids
# value is positive or asteroids value is negative then we will add into 
# stack as no element is present to collids . 
# 2=If stack has some element and top of the stack is positive and 
#top of the stack is < Mod(asteroid value) then we will pop that Top of 
# the stack .
# 3 = if Top of stack is equal to negative of that asteroid value then we
#  will pop top of the stack .
        stack = []

        for asteroid in asteroids:
            if not stack or asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(asteroid):
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(asteroid)
                elif stack[-1] == -asteroid:
                    stack.pop()

        return stack

        
# @lc code=end

