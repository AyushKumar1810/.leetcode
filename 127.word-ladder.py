#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
from collections import deque
#NOTE: our Algo will be like that  It's like a graph and we will do BFS on it 
'''
        hit (level 1)
         |
    ---------------
    |    |    |    |
   hot  git  hat  hxt  (level 2)
    |    |    |    |
   dot  git  dat  dxt  (level 3)
    |         |    |
   dog       dag  dxt  (level 4)
              |
             cog  (level 5)



Breadth-First Search (BFS) Approach:
BFS is an algorithm used for traversing or searching tree or graph data structures. In this problem, BFS helps us efficiently find the shortest transformation sequence from the start word to the target word.

BFS Algorithm:

Start from the beginWord and add it to the queue along with its initial level, which is 1.

While the queue is not empty, do the following:
a. Pop the front element (current word) and its level from the queue.
b. Check if the current word is equal to the endWord. If it is, we have found the target word, and we can return the current level as the result.
c. For each character in the current word, try all possible transformations by replacing it with all lowercase alphabets ('a' to 'z').
d. If the new word (formed by the transformation) is in the word list, it means it is a valid word. Remove it from the word list to mark it as visited and avoid revisiting it.
e. Add the new word and the incremented level to the queue for further exploration in the next BFS level.
f. Continue the BFS traversal until either the endWord is found (in which case we return the level) or there are no more words left in the queue to explore.
g. If we exhaust all possible transformations and cannot reach the endWord, we return 0, indicating that it is impossible to reach the target word.

Now, let's examine the code for the BFS solution:

python
Copy code
from collections import deque

def ladderLength(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0

    wordSet = set(wordList)
    queue = deque([(beginWord, 1)])

    while queue:
        current_word, level = queue.popleft()

        if current_word == endWord:
            return level

        for i in range(len(current_word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                new_word = current_word[:i] + char + current_word[i+1:]
                if new_word in wordSet:
                    wordSet.remove(new_word)
                    queue.append((new_word, level + 1))

    return 0
Explanation of the Code:

The function ladderLength(beginWord, endWord, wordList) takes the beginWord and endWord as the start and target words, respectively, and wordList as a list of words in the dictionary.

If the endWord is not in the wordList, it is impossible to reach the target word, so the function returns 0.

We create a wordSet to store the words in the wordList for efficient lookup during BFS. This helps us quickly check if a word is in the dictionary and if it has been visited.

We use a queue to perform BFS traversal. Each element in the queue is a tuple containing the current word and the level (number of transformations) it is at.

We add the beginWord to the queue with an initial level of 1.

While the queue is not empty, we pop the front element (current word) and its level from the queue.

We check if the current word is equal to the endWord. If it is, we have found the target word, so we return the current level as the result.

For each character in the current word, we try all possible transformations by replacing it with all lowercase alphabets ('a' to 'z').

If the new word (formed by the transformation) is in the wordSet, it means it is a valid word in the dictionary. We remove it from the wordSet to mark it as visited and avoid revisiting it.

We add the new word and the incremented level to the queue for further exploration in the next BFS level.

The BFS traversal continues until either the endWord is found (in which case we return the level) or there are no more words left in the queue to explore.

If we exhaust all possible transformations and cannot reach the endWord, we return 0, indicating that it is impossible to reach the target word.

Example:
Let's use the example we discussed earlier to illustrate how the BFS algorithm works:

makefile
Copy code
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
beginWord = "hit"
endWord = "cog"
Initially, the queue contains the tuple ("hit", 1) with the level set to 1.

Pop the front element ("hit", 1) from the queue.
Try all possible transformations of "hit": "ait", "bit", ..., "zit", "hat", "hbt", ..., "hzt."
Since "hot" and "hat" are valid words, add them to the queue with their respective levels: ("hot", 2) and ("hat", 2).
The queue now contains two elements: ("hot", 2) and ("hat", 2).
Pop the front element ("hot", 2) from the queue.
Try all possible transformations of "hot": "aot", "bot", ..., "zot", "hot", "hob", ..., "hoz."
Since "dot" is a valid word, add it to the queue with its level: ("dot", 3).
The queue now contains one element: ("hat", 2) and ("dot", 3).
Continue the BFS traversal, exploring all possible transformations and adding valid words to the queue.
Eventually, we find the endWord "cog" at level 5, and we return the level 5 as the minimum number of transformations required to reach the target word.
In this example, the shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> "cog" with 5 transformations.

The BFS approach efficiently finds the shortest transformation sequence by exploring nodes in the same level before moving to the next level, making it the preferred approach for this problem.
'''
class Solution:
    def ladderLength(self,beginWord, endWord, wordList):
    # If the endWord is not in the wordList, it is impossible to reach the target word
        if endWord not in wordList:
            return 0

    # Convert the wordList to a set for faster lookup
        wordSet = set(wordList)

    # Create a queue for BFS traversal. Each element in the queue is a tuple containing the current word and its level.
        queue = deque([(beginWord, 1)])

        while queue:
        # Pop the front element (current word) and its level from the queue
            current_word, level = queue.popleft()

        # If the current word is equal to the endWord, we have found the target word
            if current_word == endWord:
                return level

        # Try all possible transformations of the current word by replacing each character with 'a' to 'z'
            for i in range(len(current_word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                # Form a new word by replacing the character at index 'i' with 'char'
                    new_word = current_word[:i] + char + current_word[i+1:]

                # If the new word is in the wordSet (valid word in the dictionary), we remove it from the wordSet to mark it as visited
                    if new_word in wordSet:
                        wordSet.remove(new_word)

                    # Add the new word and the incremented level to the queue for further exploration in the next BFS level
                        queue.append((new_word, level + 1))

    # If we exhaust all possible transformations and cannot reach the endWord, return 0 (impossible to reach the target word)
        return 0        
# @lc code=end

