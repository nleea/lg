class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        last_one = len(nums) - 2

        while last_one >= 0 and nums[last_one] >= nums[last_one + 1]:
            last_one -= 1
        

        for i in reversed(range(last_one, len(nums))):
            if nums[i] > nums[last_one]:
                nums[i], nums[last_one] = nums[last_one], nums[i]
                break

        nums[last_one + 1 :] = reversed(nums[last_one + 1 :])


        if last_one < 0:
            nums.sort()



s = Solution()

s.nextPermutation([1, 3, 2])
