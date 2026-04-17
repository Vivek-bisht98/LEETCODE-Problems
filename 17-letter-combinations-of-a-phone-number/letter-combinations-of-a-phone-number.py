class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        my_dict={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        result=[]
        self.solve(0,[],result,digits,my_dict)
        return result

    def solve(self,index,subset,result,digits,my_dict):
        if index==len(digits):
            result.append("".join(subset))
            return

        for ch in my_dict[digits[index]]:
            subset.append(ch)
            self.solve(index+1,subset,result,digits,my_dict)
            subset.pop()