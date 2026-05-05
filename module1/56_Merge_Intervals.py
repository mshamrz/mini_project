class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]
        for start, end in intervals[1:]:
            last = result[-1]
            if start <= last[1]:
                last[1] = max(last[1], end)
            else:
                result.append([start, end])
        return result
