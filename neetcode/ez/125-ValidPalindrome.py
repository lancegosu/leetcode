# Link: https://leetcode.com/problems/valid-palindrome/
# Problem:
# A phrase is a palindrome if, after converting all uppercase letters into lowercase 
# letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # phrase = []
        # s = s.lower()
        # for i in s:
        #     if i.isalnum():
        #         phrase.append(i)
        # print(phrase)
        # if phrase == phrase[::-1]:
        #     return True
        # else:
        #     return False

        s = s.lower()
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True