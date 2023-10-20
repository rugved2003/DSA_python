class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map1 = []
        map2 = []
        for i in s:
            map1.append(s.index(i))
        for i in t:
            map2.append(t.index(i))
        if map1 == map2:
            return True

        return False

        
