class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = s.replace(" ", "")
        a, b = 0, len(news) - 1
        

        while a < b:
            if news[a].isalnum() and news[b].isalnum():
                if news[a].lower() != news[b].lower():
                    return False
                a += 1
                b -= 1
            elif news[a].isalnum():
                b -= 1
            else:
                a += 1

        return True