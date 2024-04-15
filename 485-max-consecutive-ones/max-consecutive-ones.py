class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        t = 0
        for i in nums:
            if i == 1:
                t += 1
            else: 
                t = 0

            m = max(m, t)

        return m
