class Solution:
    def isValid(self, s: str) -> bool:
        HashMap = {")" : "(", "]" : "[", "}": "{"}
        stack = []

        


        for bracket in s:
            if bracket in HashMap.values():
                stack.append(bracket)

            elif not stack or HashMap[bracket] != stack.pop():
                return False
        
        if not stack:
            return True
        return False
 