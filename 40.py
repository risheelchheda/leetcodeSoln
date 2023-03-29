def solve(start,target,path,res):
            if target<0:
                return
            if target==0 and path not in res:
                res.append(path)
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                solve(i+1,target-candidates[i],path+[candidates[i]],res)
        
        candidates.sort()
        res=[]
        if sum(candidates)<target:
            return res
        if sum(candidates)==target:
            return [candidates]
        solve(0,target,[],res)
        return res
