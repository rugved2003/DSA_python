class Solution:
    def columnWithMaxZeros(self,arr,N):
        
        # code here 
        max_zeros = 0
        max_zero_col = -1
        
        for col in range(N):
            zero_count = 0
            for row in range(N):
                if arr[row][col] == 0:
                    zero_count += 1
                    
            if zero_count > max_zeros:
                max_zeros = zero_count
                max_zero_col = col
                
        return max_zero_col
