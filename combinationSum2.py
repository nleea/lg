def combinationSum(nums, target):
    nums.sort()
    result = []

    def dfs(currIndex, remaining, currList):
        if remaining == 0:
            result.append(currList[:])
            return
        for i in range(currIndex, len(nums)):
            if nums[i] > remaining:
                break
            if i > currIndex and nums[i] == nums[i - 1]:
                continue
            currList.append(nums[i])
            dfs(i + 1, remaining - nums[i], currList)
            currList.pop()

    dfs(0, target, [])
    return result


print(combinationSum([3, 1, 3, 5, 1, 1], 8))
