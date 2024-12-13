# Link: https://leetcode.com/problems/valid-anagram/description/
# Problem:
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = {}
        word2 = {}
        for i in s:
            word1[i] = word1.get(i, 0) + 1
        for j in t:
            word2[j] = word2.get(j, 0) + 1
        
        if word1 == word2:
            return True
        else:
            return False