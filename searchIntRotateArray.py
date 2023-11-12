class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while True:
            mid = (left + right) // 2

            if nums[left] <= nums[mid]:
                if nums[left] <= target and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                if nums[left] == target:
                    return left

                left += 1

            if nums[mid] == target:
                return mid

            if left > right:
                return -1


s = Solution()
print(s.search([5, 1, 3], 5))
