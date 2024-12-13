# Link: https://leetcode.com/problems/two-sum/
# Problem:
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

class Solution(object):
    def twoSum(self, nums, target):
        # for i in range(len(nums) - 1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # time complexity: O(n^2)
        # space complexity: O(1)            

        # prep
        storage = {}
        for i in range(len(nums)):
            storage[nums[i]] = i
        
        # check
        for i in range(len(nums)):
            num1 = nums[i]
            num2 = target - num1
            if num2 in storage and i != storage[num2]:
                return [i, storage[num2]]