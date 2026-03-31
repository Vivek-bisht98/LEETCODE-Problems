class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxi=0
        zeros=0
        i=j=0
        my_set=set()
        while j<len(nums):
            if nums[j]==0:
                zeros+=1
            if zeros>k:
                if nums[i]==0:
                    zeros-=1
                i+=1
            if zeros<=k:
                maxi=max(maxi,j-i+1)
            j+=1

        return maxi
        