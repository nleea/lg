def jump(nums):

    jumps = 0
    curr_end = 0
    curr_farthest = 0
    n = len(nums)

    for i in range(n - 1):
        curr_farthest = max(curr_farthest, i + nums[i])
        if i == curr_end:
            jumps += 1
            curr_end = curr_farthest
    return jumps


print(jump([2, 3, 0, 1, 4]))
