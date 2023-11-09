class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = 10**9 + 7
        count = 1  # Initialize count to 1 to account for single-character substrings
        result = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                result = (result + (count * (count + 1) // 2)) % mod
                count = 1

        # Add the count for the last homogeneous substring
        result = (result + (count * (count + 1) // 2)) % mod

        return result
        
