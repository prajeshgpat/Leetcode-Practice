class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        diff = {}
        for i in range(len(nums)):
            if nums[i] in diff:
                return [diff[nums[i]], i]
            else:
                diff[target - nums[i]] = i


exampleInputs = [([2, 7, 11, 15], 9), ([3, 2, 4], 6), ([3, 3], 6)]
for nums, target in exampleInputs:
    print(Solution().twoSum(nums, target))
