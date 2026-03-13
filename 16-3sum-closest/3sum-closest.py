class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        ans=[]
        max_diff=float('inf')
        res_sum=0
        for k in range(len(nums)-2):
            if k>0 and nums[k]==nums[k-1]:
                k+=1
            else:
                i=k+1
                j=len(nums)-1
                while i<j:
                    sum=nums[i]+nums[j]+nums[k]
                    diff=abs(sum-target)
                        
                    if sum==target:
                        return sum
                    elif sum<target:
                        i+=1
                        if max_diff>diff:
                            max_diff=diff
                            res_sum=sum
                            
                    else:  
                        j-=1
                        if max_diff>diff:
                            max_diff=diff
                            res_sum=sum
                            
                   
        return res_sum

                
                    
                


        
        