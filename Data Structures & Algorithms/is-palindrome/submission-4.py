class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = s.strip(" ")
        right = len(s2) - 1 
        left = 0


        while left < right:
            if not s2[left].isalnum():
                left += 1 
                continue
            
            elif not s2[right].isalnum():
                right -= 1
                continue

            elif s2[left].upper() != s2[right].upper():
                return False
            
            left += 1 
            right -= 1

        return True
        