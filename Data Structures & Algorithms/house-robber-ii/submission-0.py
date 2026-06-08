class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        def helper(arr):
            rob1, rob2 = 0, 0

            for n in arr:
                newRob = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = newRob

            return rob2

        return max(
            helper(nums[:-1]),  # bỏ nhà cuối
            helper(nums[1:])    # bỏ nhà đầu
        )