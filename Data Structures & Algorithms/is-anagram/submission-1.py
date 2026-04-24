class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = [0] * 26

        for ch in s:
            counts[ord(ch) - ord('a')] += 1

        for ch in t:
            idx = ord(ch) - ord('a')
            counts[idx] -= 1
            if counts[idx] < 0:   # t has too many of some letter
                return False

        return True  
        