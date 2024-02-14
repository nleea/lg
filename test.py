def twoSum(nums: int, target: int):
    base = 0
    index = base + 1
    length = len(nums)

    if length == 2:
        return [0, 1]

    while base <= length - 1:

        if index == length:
            base += 1
            index = base + 1

        if nums[base] + nums[index] == target:
            return [base, index]

        index += 1


# print(twoSum([2, 7, 11, 15], 9))


def BitmapHoles(strArr):

    # code goes here

    holes = 1
    for i in range(len(strArr)):
        h = strArr[i]
        for j in range(len(h)):

            if h[j] == "0":

                if i > 0 and strArr[i - 1][j] == "0":
                    continue
                if i < len(strArr) - 1 and strArr[i + 1][j] == "0":
                    continue
                if j > 0 and h[j - 1] == "0":
                    continue
                if j < len(strArr) - 1 and h[j + 1] == "0":
                    continue

                holes += 1

    return holes

