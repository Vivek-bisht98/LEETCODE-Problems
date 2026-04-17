class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result=[]
        arr=[1,2,3,4,5,6,7,8,9]
        self.solve(0,n,[],result,k,arr)
        return result
    
    def solve(self,index,target,subset,result,k,arr):
        if len(subset)==k:
            if target==0:
                result.append(subset.copy())
            return
        if index==len(arr):
            return
        subset.append(arr[index])
        sum=target-arr[index]
        self.solve(index+1,sum,subset,result,k,arr)
        subset.pop()
        sum=target
        self.solve(index+1,sum,subset,result,k,arr)
        

        