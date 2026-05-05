class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(': ')', '{': '}', '[': ']'}

        for ch in s:
            if ch in pairs:  # opening
                stack.append(ch)
            else:  # closing
                if not stack or pairs[stack.pop()] != ch:
                    return False

        return not stack