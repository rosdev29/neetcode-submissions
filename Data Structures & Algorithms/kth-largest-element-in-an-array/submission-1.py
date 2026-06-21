import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k

        def quick_select(l, r):
            pivot_idx = random.randint(l, r)
            nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]

            pivot = nums[r]
            p = l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1

            nums[p], nums[r] = nums[r], nums[p]

            if p == target:
                return nums[p]
            elif p < target:
                return quick_select(p + 1, r)
            else:
                return quick_select(l, p - 1)

        return quick_select(0, len(nums) - 1)