class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        counts = {0: 1}
        run = 0
        for num in nums:
            run += num
            count += counts.get(run - k, 0)
            counts[run] = counts.get(run, 0) + 1
        return count