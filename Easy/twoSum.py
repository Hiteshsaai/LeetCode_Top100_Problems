class Solution:
    def twoSum(self, nums, target):
        ## Time O(n) || Space O(n)
        if len(nums) <= 1:
            return []

        visited = {}

        for i in range(len(nums)):

            targetNum = target - nums[i]
            if targetNum in visited:
                return [visited[targetNum], i]

            visited[nums[i]] = i

        return []


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))