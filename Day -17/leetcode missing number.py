class Solution:
    
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        # ans = 0
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return nums[-1]+1
