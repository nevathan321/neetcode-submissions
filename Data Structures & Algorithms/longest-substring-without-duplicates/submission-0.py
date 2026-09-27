class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = set()
        best = 0 
        left = 0    
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[left])
                left += 1
            window.add(s[r])
            best = max(len(window), best)
    
        return best

        