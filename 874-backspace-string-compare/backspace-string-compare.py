class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        arrS=[]
        arrT=[]
        for i in s:
            if i=='#':
                if len(arrS)==0:
                    continue
                else:
                    arrS.pop()
            else:
                arrS.append(i)
        for i in t:
            if i=='#':
                if len(arrT)==0:
                    continue
                else:
                    arrT.pop()
            else:
                arrT.append(i)
        if arrS==arrT:
            return True
        else:
            return False



        