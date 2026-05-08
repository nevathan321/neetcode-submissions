class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = { '(' : ')', '[' : ']', '{' : '}'} 

        for letter in s: 
            if letter in pairs: 
                stack.append(letter)
                continue

        
            if not stack or pairs[stack.pop()] != letter:
                return False

        return not stack
                 