class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    len_n = len(nums)
 
    if len_n == 0 or nums is None:
      return nums
 
    ans = [1] * len_n 
 
    for i in range(1, len_n):
      ans[i] = nums[i - 1] * ans[i - 1]
    right = 1
    
    for i in range(len_n -1, -1, -1):
      ans[i] *= right
      right *= nums[i]
    
    return ans