class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0
        p,n = 1,len(nums)
        i = c= 0
        for j in range (n):
            p*=nums[j]
            while p>= k and i<= j:
                p/= nums[i]
                i+=1
            c+=j-i+1
        return c
