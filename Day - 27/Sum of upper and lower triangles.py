class Solution:
    
    #Function to return sum of upper and lower triangles of a matrix.
    def sumTriangles(self,matrix, n):
        # code here 
        upper_sum = 0
        lower_sum = 0
        
        for i in range(n):
            for j in range(n):
                if i <= j:
                    upper_sum += matrix[i][j]
                    
        for i in range(n):
            for j in range(n):
                if j <= i:
                    lower_sum += matrix[i][j]
                    
        return upper_sum, lower_sum
