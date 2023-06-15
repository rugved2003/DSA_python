class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hset = set()
        for i in nums:
            if i in hset:
                return True
            else:
                hset.add(i)