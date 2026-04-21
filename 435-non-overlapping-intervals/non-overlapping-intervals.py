class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        count=0
        lastkey=intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0]<lastkey:
                count+=1
            else:
                lastkey=intervals[i][1]
        return count