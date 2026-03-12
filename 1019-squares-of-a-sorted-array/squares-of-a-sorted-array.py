class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a=[]
        b=[]
        arr=[]
        for i in range(len(nums)):
            if nums[i]>=0:
                a.append(nums[i]*nums[i])
            else:
                b.append(nums[i]*nums[i])
        b.reverse()
        i=0
        j=0
        while i<len(a) and j<len(b):
            if a[i]>b[j]:
                arr.append(b[j])
                j+=1
            else:
                arr.append(a[i])
                i+=1
        while i<len(a):
            arr.append(a[i])
            i+=1
        while j<len(b):
            arr.append(b[j])
            j+=1
        return arr
        