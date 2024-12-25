class Solution:
  def shortestDistance(
      self,
      wordsDict: list[str],
      word1: str,
      word2: str,
) -> int:
    ans = len(wordsDict) # the maximum possible value of the answer 
    index1 = -1  # wordsdict[index1] == word1 
    index2 = -1  # wordsdict[index2] == word2
    for i, word in enumerate(wordsDict): # iterate through the wordsDict 
        if word == word1: # if the word is word1 , update index1 
            index1 = i
            if index2 != -1: # if index2 is not -1 , then update the answer 
            ans = min(ans, index1 - index2) # update the answer with the minimum of the current answer and the difference between the two indexes 
        if word == word2: # if the word is word2 , update index2 
            index2 = i
            if index1 != -1:
                ans = min(ans, index2 - index1) # update the answer with the minimum of the current answer and the difference between the two indexes 
        return ans
    
#other way to solve the problem
class Solution:
   def shortestDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
        ans = len(wordsDict) # the maximum possible value of the answer
        index1 = -1
        index2 = -1
        for i, word in enumerate(wordsDict): # iterate through the wordsDict
            if word == word1: # if the word is word1 , update index1
                index1 = i
            if word == word2:
                index2 = i
            if index1 != -1 and index2 != -1:
                ans = min(ans, abs(index1 - index2))
        return ans
   