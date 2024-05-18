class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)        
        if shortest == "": return ""

        for ind, ch in enumerate(shortest):
            for s in strs:
                if s[ind] != ch:
                    return shortest[:ind]

        return shortest

#This part only contains the solution. The codes may not work directly.
#Therefore, you need to copy the code to the required leetcode question solution section to verify it. After selecting Python3, copy it to the answer section.