class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=len(s)
        if l==0:
            return 0
        dicts={}
        max_len=0
        start=0
        for i in range(l):
            if s[i] in dicts and start<=dicts[s[i]]:
                start = dicts[s[i]]+1
            else:
                max_len=max(max_len,i-start+1)
            dicts[s[i]]=i
        return max_len
    
#This part only contains the solution. The codes may not work directly.
#Therefore, you need to copy the code to the required leetcode question solution section to verify it. After selecting Python3, copy it to the answer section.