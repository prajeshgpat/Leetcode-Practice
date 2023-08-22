class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        temp = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                temp.append(newInterval)
                return temp + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                temp.append(intervals[i])
            else:
                newInterval = [
                    min(intervals[i][0], newInterval[0]),
                    max(intervals[i][1], newInterval[1]),
                ]

        temp.append(newInterval)
        return temp


# Scheduler
testInputs = [
    [[[1, 3], [6, 9]], [2, 5]],
    [[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]],
]
for intervals, newInterval in testInputs:
    print(Solution().insert(intervals, newInterval))
