class Solution:
    def twoSum(self, numbers: List[int], num: int) -> List[List[int]]:
        res = []
        i, j = 0, len(numbers) - 1
        while j > i:
            s = numbers[i] + numbers[j]
            if s == -num:
                res.append([num, numbers[i], numbers[j]])
                i += 1
                j -= 1
                while i < j and numbers[i] == numbers[i - 1]:
                    i += 1
                while i < j and numbers[j] == numbers[j + 1]:
                    j -= 1
            elif s > -num:
                j -= 1
            else:
                i += 1
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            answer += self.twoSum(nums[i + 1:], nums[i])
        return answer