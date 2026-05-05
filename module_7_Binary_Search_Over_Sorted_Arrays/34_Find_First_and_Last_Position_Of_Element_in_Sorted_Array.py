from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_right():
            result = - 1
            min_i, max_i = 0, len(nums) - 1
            while min_i <= max_i:
                a = (min_i + max_i) // 2
                if nums[a] > target:
                    max_i = a - 1
                else:
                    min_i = a + 1
                if nums[a] == target:
                    result = a
            return result
        def find_left():
            result = - 1
            min_i, max_i = 0, len(nums) - 1
            while min_i <= max_i:
                a = (min_i + max_i) // 2
                if nums[a] >= target:
                    max_i = a - 1
                else:
                    min_i = a + 1
                if nums[a] == target:
                    result = a
            return result
        return [find_left(), find_right()]
