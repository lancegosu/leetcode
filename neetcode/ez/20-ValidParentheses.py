# Link: https://leetcode.com/problems/valid-parentheses/
# Problem:
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# - Open brackets must be closed by the same type of brackets.
# - Open brackets must be closed in the correct order.
# - Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        # brackets = []
        # items = { ")":"(", "]":"[", "}":"{" }

        # for i in s:
        #     if i in items:
        #         if brackets and brackets[-1] == items[i]:
        #             brackets.pop()
        #         else:
        #             return False
        #     else:
        #         brackets.append(i)
        # return True if not brackets else False

        # brackets = []
        # items = { "(":")", "[":"]", "{":"}" }

        brackets = []
        items = { "(":")", "[":"]", "{":"}" }

        for i in s:
            if i in items:
                brackets.append(i)
            elif brackets and items[brackets[-1]] == i:
                brackets.pop()
            else:
                return False

        return True if not brackets else False