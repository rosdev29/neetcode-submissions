class Solution:
    def twoSum(self, nums, target):

        seen = {}

        for i in range(len(nums)):

            complement = target - nums[i]

            # nếu số cần tìm đã tồn tại
            if complement in seen:
                return [seen[complement], i]

            # lưu giá trị và index
            seen[nums[i]] = i