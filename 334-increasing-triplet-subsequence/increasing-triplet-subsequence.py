class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = float(inf)
        j = float(inf)
        for k in range(len(nums)):
            if i >= nums[k]: i = nums[k]
            elif j >= nums[k] : j = nums[k]
            else: return True
        return False
            