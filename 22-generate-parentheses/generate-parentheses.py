class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        bracket=[""]*(n*2)
        result=[]
        solve(0,0,bracket,result)
        return result
def solve(index,target,bracket,result):
    if target<0:
        return
    if target>(len(bracket)//2):
        return
    if index==len(bracket):
        if target==0:
            result.append("".join(bracket))
        return
    bracket[index]="("
    sum=target+1
    solve(index+1,sum,bracket,result)
    bracket[index]=")"
    sum=target-1
    solve(index+1,sum,bracket,result)