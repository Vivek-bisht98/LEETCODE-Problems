class Solution:
    def isPalindrome(self, s: str) -> bool:
        res="".join(filter(str.isalnum,s))
        res=res.lower()
        i=0
        j=len(res)-1
        is_palindrome=True
        while i<j:
            if res[i]==res[j]:
                i+=1
                j-=1
            else:
                is_palindrome=False
                break
        return is_palindrome


        