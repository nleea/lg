def merge(intervals):
    if len(intervals) <= 1:
        return intervals

    intervals.sort(key=lambda x: x[0])

    base = []
    base.append(intervals[0])

    for i in range(1, len(intervals)):
        current = intervals[i]
        last_merged = base[-1]
        if current[0] <= last_merged[1]:
            base[-1] = [last_merged[0], max(last_merged[1], current[1])]
        else:
            base.append(current)

    return base

print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
