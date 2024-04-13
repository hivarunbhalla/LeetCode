class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {
            x : nums.count(x) for x in set(nums)
        }

        n = len(nums) // 2
        for k, fre in freq.items():
            if fre > n:
                return k

        return 0