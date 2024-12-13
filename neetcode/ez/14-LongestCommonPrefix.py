# Link: https://leetcode.com/problems/longest-common-prefix/
# Problem:
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # check each letter for each element in the list
            # f, f, f
        # if they are all the same, store them in a string
        # if they are not, don't continue the loop and return the string
        # or return empty string if no match
        # only need the minimum length of strings
        answer = ""
        first_word = strs[0]
        # get the length of first word
        for i in range(len(first_word)):
            for word in strs[1:]:
                # compare if first word letter matches other word letters at the same index
                if i >= len(word) or first_word[i] != word[i]:
                    return answer
            answer += first_word[i]
        
        return answer
        
        # OR, use first string as reference