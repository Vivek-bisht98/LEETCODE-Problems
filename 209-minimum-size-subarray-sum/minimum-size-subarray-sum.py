class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        i=j=0
        window_sum=0
        min_len=float('inf')

        while j<n:
            window_sum+=nums[j]
            while window_sum>=target:
                min_len=min(min_len,j-i+1)
                window_sum-=nums[i]
                i+=1
            j+=1
        if min_len==float("inf"):
            return 0 
        else:
            return min_len

        