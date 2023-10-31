class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        c = 0
        for char in columnTitle:
            c = c * 26 + (ord(char)- 64)
        return c        
