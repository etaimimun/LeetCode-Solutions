class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i in range(len(nums)):
            numbers[nums[i]] = i
        for i in range(len(nums)):
            y = target - nums[i]
            if y in numbers and numbers[y] != i:
                return [i, numbers[y]]

            