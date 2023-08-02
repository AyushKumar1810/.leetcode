#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start

#NOTE- It's very beautiful question as we can see we have to find anagram , so our approach will be  ::
#1. we will find length of subarray p and then we will store it in hashmap along with it's count.
#2. then we will initiallize two pointer left and right on array s , initially at 0 and right will traverse till size of p and then after i will increament .
#3.As j is traversing we will kepp comparing arr[j] with hashmap if it's present then good otherwise increament 
class Solution:
    def findAnagrams(self,s,p):
        result = []  # List to store the starting indices of anagrams
        target_count = {}  # Dictionary to store the count of characters in the target string 'p'
        window_count = {}  # Dictionary to store the count of characters in the current window of 's'

    # Count the occurrences of characters in the target string 'p' and store them in 'target_count'
        for char in p:
            target_count[char] = target_count.get(char, 0) + 1

    # Initialize left and right pointers for the sliding window
        left, right = 0, 0

        while right < len(s):
        # Expand the window by adding the current character to 'window_count'
            window_count[s[right]] = window_count.get(s[right], 0) + 1

        # When the window size becomes equal to the length of 'p'
            if right - left + 1 == len(p): # Chceking window size is equal to length of p
            # Check if the 'window_count' matches the 'target_count', which means we have an anagram
                if window_count == target_count:
                # Add the starting index of the window (left pointer) to the result list
                    result.append(left)

            # Move the window to the right by incrementing the left pointer
            # Remove the leftmost character from 'window_count'
                window_count[s[left]] -= 1  # decreament count 
                if window_count[s[left]] == 0:
                    del window_count[s[left]] #deleting value
                left += 1

        # Move the right pointer to expand the window
            right += 1 # If size if not equal to size of p then increase right pointer till 

        return result



        
# @lc code=end

