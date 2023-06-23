class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        r = 1
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]:
                nums[r] = nums[i]
                r += 1
        return r
