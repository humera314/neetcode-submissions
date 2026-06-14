class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key= lambda x: x[0])
        merge=[intervals[0]]
        
        for start, end in intervals:
            last=merge[-1][1]
            

            if last >= start:
                merge[-1][1]= max(last, end)
            else:
                merge.append([start, end])
        return merge