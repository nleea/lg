class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        right = len(nums) - 1
        left = 0
        i = -1
        j = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                i = mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        right = len(nums) - 1
        left = 0

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                j = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return [i, j]


s = Solution()
print(s.searchRange([1, 3], 3))
