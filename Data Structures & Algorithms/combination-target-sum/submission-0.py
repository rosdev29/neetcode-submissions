class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        res = []

        def backtrack(start, curr, total):
            if total == target:
                res.append(curr[:])
                return

            if total > target:
                return

            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtrack(i, curr, total + nums[i])
                curr.pop()

        backtrack(0, [], 0)
        return res