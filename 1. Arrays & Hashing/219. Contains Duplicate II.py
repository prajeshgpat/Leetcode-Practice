class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dupl = {}
        for i in range(len(nums)):
            if nums[i] in dupl:
                if abs(dupl[nums[i]] - i) <= k:
                    return True
                else:
                    dupl[nums[i]] = i
            else:
                dupl[nums[i]] = i
        return False


testInputs = [[[1, 2, 3, 1], 3], [[1, 0, 1, 1], 1], [[1, 2, 3, 1, 2, 3], 2]]
for nums, k in testInputs:
    print(Solution().containsNearbyDuplicate(nums, k))
