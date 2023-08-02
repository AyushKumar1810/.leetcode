#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start

##NOTE- in that question we have to replace the character k time so that we wil get the maximum lagoest substring 
#NOTE- Our approach is that we will create a Hashmap to store the value and it's count , After that we will find maximum count by goint through hashmap then we will use our main approach to find how many replacement we have to make ? the answe is that " Agar hmlog jitna window ka size hae usmain se maximum count ko substrct k de to No of replacement nikal jaega " {for eg ABABBA ,K=2  so we can Replace  2 times suppose our i=0 and j=3 so window size is 4 (j-1+1 =3-0+1 =4)  , maximum count is b-2 and a-2 so we have to put into formula replacement=Window size - max count is equal to 4-2=2 so we need 2 replacemnet and we will check our replacement with k it should be less than or equal to k for further processing}

##NOTE:we will do follwoing things :::
#1. We will create A HashMap to store character and it's count 
#2. Then we will get maximum count of character from hashmap {complexivity with O(26) AS we have 26 character so we will go through every charcter and compare it's count}
#3. then we will think of how can we get "No of element to be replaced " It's quite simple After finding max character count , we will find our window size and then if we substract window size with max chatacter count then we will get "No of character we need to replace "
#4. we will make sure that "No of character we need to replace "will less than or equal to k
#i.e char_replacement <=k ..If it's valid till we will increament our j pointer j=j+1 , if it's invalid then we will increament i pointer i=i+1 

#NOTE-In short , initially i and j will be on 0th index and we will take that character and it's count and check with our condition , then increase j and again take into hashmap and take it's value and count and again check the comdtion and so on .... at any point it will invalid then we will increament i =i+1 and be carefull before increament  i we will hve to remove arr[i] from hashmap , means we have to decreament the count .. and we will update our result with our window size {J-i+1}

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Initialize a dictionary to store the count of each character in the window
        count = {}
        # Initialize the result variable to store the length of the longest substring
        result = 0
        # Initialize the left_pointer to represent the left boundary of the sliding window
        left_pointer = 0
        
        # Loop through the characters of the input string using right_pointer
        for right_pointer in range(len(s)):
            # Update the count of the current character in the count dictionary
            count[s[right_pointer]] = 1 + count.get(s[right_pointer], 0)
            
            # Check whether the current window size minus the maximum frequency of any character in the window is greater than k
            while (right_pointer - left_pointer + 1) - max(count.values()) > k:
                # Shrink the window from the left side
                # Reduce the count of the character at the left boundary
                count[s[left_pointer]] -= 1
                # Increment the left_pointer to move the window to the right
                left_pointer += 1
            
            # After shrinking the window, update the result variable to store the maximum length of the substring seen so far
            result = max(result, right_pointer - left_pointer + 1)
        
        # Finally, return the result, which represents the length of the longest substring with the same repeating character
        # that can be obtained by replacing at most k characters
        return result

# @lc code=end