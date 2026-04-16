class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result=[]
        self.solve(0,target,candidates,[],result)
        return result
    def solve(self,index,target,candidates,subset,result):
        if target==0:
            result.append(subset.copy())
            return
        elif target<0:
            return
        if index==len(candidates):
            return
        for i in range(index,len(candidates)):
            if i>index and candidates[i]==candidates[i-1]:
                continue
            subset.append(candidates[i])
            self.solve(i+1,target-candidates[i],candidates,subset,result)
            subset.pop()
        