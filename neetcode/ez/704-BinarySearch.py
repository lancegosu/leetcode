# Link: https://leetcode.com/problems/binary-search/
# Problem:
# Given an array of integers nums which is sorted in ascending order, 
# and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        # for i in range(len(nums)):
        #     m = (left + right) // 2
        #     if nums[i] < target:
        #         left = m + 1
        #     elif nums[i] > target:
        #         right = m - 1
        #     elif nums[i] == target:
        #         return i

        # return -1

        while left <= right:
            m = (left + right) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                left = m + 1
            else:
                right = m - 1
        
        return -1