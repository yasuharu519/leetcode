class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v1 in enumerate(nums):
            for j, v2 in enumerate(nums[i+1:], i+1):
                if (v1 + v2) == target:
                    return [i, j]
