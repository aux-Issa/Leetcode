# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {')':'(', '}':'{', ']':'['}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == []:
                    return False
                
                if dict[char] != stack.pop():
                    return False
            else:
                return False
        # if stack == []:
        return stack == []
