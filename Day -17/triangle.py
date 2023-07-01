class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = {(0,0):triangle[0][0]}
        for i in range(1,len(triangle)):
            for j in range (i+1):
                dp[(i,j)] = triangle[i][j] + min(dp.get((i-1,j), float("inf")),dp.get((i-1,j-1),float("inf")))
        return min(dp[(len(triangle)-1,j)] for j in range(len(triangle[-1])))
