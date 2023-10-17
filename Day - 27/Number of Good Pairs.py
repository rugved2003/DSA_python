class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        res = 0
        for num in nums:
            if num in count:
                res += count[num]
                count[num] += 1
            else:
                count[num] = 1

        return res
