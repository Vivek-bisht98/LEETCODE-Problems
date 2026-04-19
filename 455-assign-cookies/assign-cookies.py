class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count=0
        i=0
        j=0
        g.sort()
        s.sort()
        while j<len(s):
            if i==len(g):
                break
            elif g[i]<=s[j]:
                count+=1
                i+=1
            j+=1
        return count
        