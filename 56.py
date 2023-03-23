intervals.sort(key = lambda x: x[0])
        res=[intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i][0]<=res[-1][1]:
                start=min(intervals[i][0],res[-1][0])
                end=max(intervals[i][1],res[-1][1])
                res[-1]=[start,end]
            else:
                res.append(intervals[i])
        return res
