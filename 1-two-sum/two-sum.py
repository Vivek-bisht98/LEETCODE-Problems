class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i ,num in enumerate(nums):
            arr=target-num
            if arr in seen:
                return [seen[arr],i]
            seen[num]=i
            

        