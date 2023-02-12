class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = len(nums)
        for i in range(a):
            b = target - nums[i]
            if b in nums:
                index = nums.index(b)
                if i != index:
                    return [i, index]




