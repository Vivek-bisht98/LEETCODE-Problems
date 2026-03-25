class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low=0
        high=0
        my_dict={}
        maxi=0
        while high<len(s):
            if s[high] in my_dict:
                low=max(low,my_dict[s[high]]+1)
            maxi=max(maxi,high-low+1)
            my_dict[s[high]]=high

            high+=1
        return maxi
        
        