
    def maxPower(self, s: str) -> int:
        m = 0
        c = 1

        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                c += 1
            else:
                m = max(m,c)
                c = 1

        return max(m,c)
        
