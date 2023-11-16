class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        leng_01, leng_02 = len(s), len(p)
        dp = [[False] * (leng_02 + 1) for _ in range(leng_01 + 1)]
        dp[0][0] = True
        for lp in range(1, leng_02 + 1):
            if p[lp - 1] == '*':
                dp[0][lp] = dp[0][lp - 2]
        
        for i in range(1, leng_01 + 1):
            for lp in range(1, leng_02 + 1):
                if p[lp - 1] == '.' or s[i - 1] == p[lp - 1]:
                    dp[i][lp] = dp[i - 1][lp - 1]
                elif p[lp - 1] == '*':
                    dp[i][lp] = dp[i][lp - 2] or (dp[i - 1][lp] and (s[i - 1] == p[lp - 2] or p[lp - 2] == '.'))
        return dp[leng_01][leng_02]
    
#This part only contains the solution. The codes may not work directly.
#Therefore, you need to copy the code to the required leetcode question solution section to verify it. After selecting Python3, copy it to the answer section.