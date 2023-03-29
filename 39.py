def solve(start,target,path,res):
            if target<0:
                return 
            if target==0:
                res.append(path)
                return
            for i in range(start,len(candidates)):
                solve(i,target-candidates[i],path+[candidates[i]],res)

        res=[]
        solve(0,target,[],res)
        return res
