class Solution:
    def findMin(self, arr: List[int]) -> int:
        n = len(arr)
        min_ele = arr[0]
    
        # Traversing over array to
        # find minimum element
        for i in range(n) :
            if arr[i] < min_ele :
                min_ele = arr[i]
    
        return min_ele
      