# Link: https://leetcode.com/problems/find-closest-number-to-zero/
# Problem:
# Given an integer array nums of size n, return the number with the value closest to 0 in nums. 
# If there are multiple answers, return the number with the largest value.

from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        # look through the whole array (for)
        # define a variable that stores the distance
        # for each element, compare the absolute of it to how far it is from 0 and assign it to a variable
        # if the next element is closer, replace the variable with the new element
        # min_distance = abs(nums[0])
        min_element = nums[0]
        for i in nums[1::]:
            if abs(i) < abs(min_element):
                # min_distance = abs(i)
                min_element = i
            elif abs(i) == abs(min_element) and i > min_element:
                min_element = i
        
        return min_element