class Solution:
    def minMoves(nums)
        # Find the minimum element in the input array
        min_element = min(nums)
        
        # Calculate the sum of the differences between each element and the minimum element
        sum_diff = sum(nums) - len(nums) * min_element
        
        # Return the sum of the differences as the minimum number of moves required to make all array elements equal
        return sum_diff
        
