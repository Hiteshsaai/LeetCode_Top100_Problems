class Solution:
    @classmethod
    def threeSum(self, nums):

        ## Time O(n^2) || Space O(n)
        if not nums:
            return nums

        triplets = set()
        nums.sort()
        n = len(nums)
        for i in range(0, n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                currSum = nums[i] + nums[left] + nums[right]
                triplet = (nums[i], nums[left], nums[right])

                if currSum > 0:
                    right -= 1

                elif currSum < 0:
                    left += 1

                else:
                    if triplet not in triplets:
                        triplets.add(triplet)
                    left += 1
                    right -= 1

        return [list(triplet) for triplet in triplets]


if __name__ == "__main__":

    print(Solution.threeSum([-1, 0, 1, 2, -1, -4]))
