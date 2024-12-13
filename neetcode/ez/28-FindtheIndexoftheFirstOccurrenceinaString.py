# Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Problem:
# Given two strings needle and haystack, return the index of the 
# first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:        
        # i want to check if each character in needle is in haystack
        # iterate through haystack
        # check if needle can start from this
        for i in range(len(haystack)-len(needle)+1): # good for position
            same = True
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    same = False
                    break
            if same == True:
                return i

        return -1