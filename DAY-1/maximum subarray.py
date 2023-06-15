'''def maximumSubarraySum(arr):
    n = len(arr)
    maxSum = -1e8

    for i in range(0, n):
        currSum = 0
        for j in range(i, n):
            currSum = currSum + arr[j]
            if(currSum > maxSum):
                maxSum = currSum

    return maxSum

if __name__ == "__main__":
    # Your code goes here
    a = [1, 3, 8, -2, 6, -8, 5];
    print(maximumSubarraySum(a));
'''


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        maxSum = nums[0]
        minSum = sum = 0
        for i in range(n):
            sum += nums[i]
            maxSum = max(maxSum, sum - minSum)
            minSum = min(minSum, sum)

        return maxSum