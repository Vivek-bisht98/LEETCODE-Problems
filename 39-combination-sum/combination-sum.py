class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        subset=[]
        index=0
        k=0
        solve(index,k,candidates,target,subset,result)
        return result

def solve(index,k,candidates,target,subset,result):
    if k==target:
        result.append(subset.copy())
        return
    elif k>target:
        return
    if index==len(candidates):
        return
    subset.append(candidates[index])
    sum=k+candidates[index]
    solve(index,sum,candidates,target,subset,result) 
    subset.pop() 
    sum=k
    solve(index+1,sum,candidates,target,subset,result)      