class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal and len(set(s)) < len(s):
            return True

        dif = []
        for x in range(len(goal)):
            if s[x] != goal[x]:
                dif.append([s[x],goal[x]])

        if len(dif) == 2 and dif[0] == dif[-1][::-1]:
            return True
        return False
