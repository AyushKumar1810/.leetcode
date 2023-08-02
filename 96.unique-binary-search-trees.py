#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start

#NOTE=By using the dynamic programming approach and storing the previously calculated values in the dictionary, the code avoids redundant calculations. In this example, it calculates the number of unique BSTs for n = 4 in three iterations instead of recalculating it from scratch.

# This approach is efficient and can be applied to larger values of n, reducing
# We are solving using the idea is that it's just multiplacation of no of node in left with no of in right .
# For eg if we have n=4(i.e 1,2,3,4) so Suppose Root node is 1 so on left 0 will be there and on right 2 , 3 , 4 will be there , so we will multiply 1*3=3  , so we will decrease right pointer r=r-1 and left with l=l+1  , again it will go on recursivily .. for rootnode 2 ,3 like that 

class Solution:
    def numTrees(self, n: int) -> int:
        # Create a dictionary to store previously calculated values
        self.trees = {}
        self.trees[0] = 1
        self.trees[1] = 1
        self.trees[2] = 2

        # Call the helper function to calculate the number of unique BSTs
        return self.getTrees(n)

    def getTrees(self, n):
        # Check if the number of unique BSTs for 'n' has already been calculated
        if n in self.trees:
            return self.trees[n]

        # Initialize variables for the left and right subtree sizes
        l, r = 0, n-1 #initialising Right node will be n-1 and left will be 0 initially we suppose  , for root node value to 0

        # Initialize result variable
        res = 0

        # Calculate the number of unique BSTs by considering different left and right subtree sizes
        while r >= 0:
            res += (self.getTrees(l) * self.getTrees(r))
            l += 1# it will increase as root node value increases 
            r -= 1# It will decreases as root node value increases

        # Store the result in the dictionary for future use
        self.trees[n] = res
        return res

        
# @lc code=end

