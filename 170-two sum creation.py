from collections import Counter

class TwoSum:
    def __init__(self):
        self.cnt = Counter() # create a dictionary to store the count of each element in the list 
    def add(self, number: int) -> None:
        self.cnt[number] += 1 # increment the count of the number by 1 
    def find(self, value: int) -> bool:
        for x in self.cnt: # iterate through the keys of the dictionary 
            y = value - x # find the difference between the value and the key 
            if y in self.cnt: # check if the difference is present in the dictionary 
                if x != y or self.cnt[x] > 1: # if the difference is not equal to the key or the count of the key is greater than 1, return True 
                    return True
        return False
# Example 1: 
# obj = TwoSum()
# obj.add(1)
# obj.add(3)
# obj.add(5)
# obj.find(4) # returns True
# obj.find(7) # returns False
# obj.find(8) # returns False
# obj.find(9) # returns True
# obj.find(10) # returns False
# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)