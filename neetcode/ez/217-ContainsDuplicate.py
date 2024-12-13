# Link: https://leetcode.com/problems/contains-duplicate/
# Problem:
# Given an integer array nums, return true if any value appears at 
# least twice in the array, and return false if every element is distinct.

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        storage = {}
        for i in nums:
            if i in storage:
                return True
            storage[i] = i
        
        return False