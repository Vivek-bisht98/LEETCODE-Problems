class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()
        
        ans=[]
        for k in range(len(nums)-2):
            if k>0 and nums[k]==nums[k-1]:
                k+=1
            else:
                i=k+1
                j=len(nums)-1
                target=(-nums[k])
                while i<j:
                    sum=nums[i]+nums[j]
                    if sum>target:
                        j-=1
                        
                    elif sum<target:
                        i+=1
                    else:
                        ans.append([-target,nums[i],nums[j]])
                        i+=1
                        j-=1
                        while i<len(nums) and nums[i]==nums[i-1]:
                            i+=1
                        while j>=0 and nums[j]==nums[j+1]:
                            j-=1
        return ans

                
                    
                


        