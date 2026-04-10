class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ind=0
        result=[]
        subset=[]
        solve(ind,subset,result,nums)
        return result
def solve(indx,subset,result,nums):
        if indx>=len(nums):
            result.append(subset.copy())
            return
        subset.append(nums[indx])
        solve(indx+1,subset,result,nums)
        subset.pop()
        solve(indx+1,subset,result,nums)
    
