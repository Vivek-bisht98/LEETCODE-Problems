class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        my_dict={}
        l=r=0
        maxi=0
        while r<len(fruits):
            my_dict[fruits[r]]=r
            if len(my_dict)>2:
                v=min(my_dict.values())
                for key,value in my_dict.items():
                    if value==v:
                        k=key
                del my_dict[k]
                l=v+1
            
            maxi=max(maxi,r-l+1)
            r+=1
            
        return maxi