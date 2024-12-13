# Link: https://leetcode.com/problems/merge-strings-alternately/
# Problem: 
# You are given two strings word1 and word2. Merge the strings by adding letters in 
# alternating order, starting with word1. If a string is longer than the other, 
# append the additional letters onto the end of the merged string. Return the merged string.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # define a variable that stores the output
        merged_string = ""
        # iterate through each word
        for i in range(max(len(word1), len(word2))):
            # store the char from each word to the merged_string
            if i < len(word1):
                merged_string += word1[i]
            if i < len(word2):
                # pos = (len(word2) - 1) - i
                merged_string += word2[i]

        return merged_string
    
    def mergeAlternatelyReverse(self, word1: str, word2: str) -> str:
        # define a variable that stores the output
        merged_string = ""
        # iterate through each word
        for i in range(max(len(word1), len(word2))):
            # store the char from each word to the merged_string
            if i < len(word1):
                merged_string += word1[i]
            if i < len(word2):
                pos = (len(word2) - 1) - i
                merged_string += word2[pos]

        return merged_string