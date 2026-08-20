class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
            
        Counter = [0] * 26

        for _, char in enumerate(s):
            Counter[ord(char.upper()) - 65] += 1
        
        for _, char2 in enumerate(t):
            if Counter[ord(char2.upper()) - 65] > 0:
                Counter[ord(char2.upper()) - 65] -= 1
                
        for num in Counter:
            if num != 0:
                return False 
        return True
                
  