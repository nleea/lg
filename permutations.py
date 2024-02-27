def permute(nums):
    valid = []
    length = len(nums)

    def permute_rs(nums, permuted: list):
        
        for i in range(len(nums)):
            permuted.append(nums[i])
            permute_rs([x for x in nums if x != nums[i]], permuted)
            if len(permuted) == length:
                valid.append(permuted[:])
            permuted.pop()

    permute_rs(nums, [])

    return valid


print(permute([1, 2, 3]))
