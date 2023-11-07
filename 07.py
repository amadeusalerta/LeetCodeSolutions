class Solution:
    def reverse(self, x: int) -> int:
        x=list(str(x))
        x.reverse()
        factor1=""
        factor2=0
        for i in x:
            if(i!="-"):
                factor1+=i
            else:
                factor2=1
        factor1=int(factor1)
        if(factor1>(2**31)-1):
            return 0
        if(factor2==0):
            return factor1
        else:
            return -factor1

#This part only contains the solution. The codes may not work directly.
#Therefore, you need to copy the code to the required leetcode question solution section to verify it. After selecting Python3, copy it to the answer section.