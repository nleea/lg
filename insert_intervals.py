def insert(intervals: list[list], newInterval: list):

    intervals.append(newInterval)

    intervals = sorted(intervals, key=lambda x: x[0])

    base = [intervals[0]]

    for i in range(1, len(intervals)):
        if base[-1][-1] >= intervals[i][0]:
            base[-1] = [base[-1][0], max(base[-1][1], intervals[i][1])]
        else:
            base.append(intervals[i])
    return base


print(insert([[1, 3], [6, 9]], [2, 5]))
