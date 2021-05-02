class Solution:
    def maxSubArray(self, nums):

        ## Time O(n) || Space O(1)
        maxSum = float("-inf")

        runningSum = 0

        for num in nums:
            runningSum += num
            currMax = max(runningSum, num)
            if currMax > maxSum:
                maxSum = currMax

            runningSum = currMax

        return maxSum


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(nums))