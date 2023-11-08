#User function Template for python3

class Solution:
    
    #Function to return list of integers visited in snake pattern in matrix.
    def snakePattern(self, matrix): 
        N = len(matrix)
        s = []
        for i in range(N):
            if i % 2==0:
                for j in range(N):
                    s.append(matrix[i][j])
                    
            else:
                for j in range(N-1,-1,-1):
                    s.append(matrix[i][j])
                    
        return s
       # code here
