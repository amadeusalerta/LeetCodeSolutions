class Solution:
    def romanToInt(self, s):
        table = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        sm, pre = 0, 'I'
        for c in s[::-1]: 
            if table[c] < table[pre]:
                sm, pre = sm - table[c], c  
            else:
                sm, pre = sm + table[c], c
        return sm
    
#This part only contains the solution. The codes may not work directly.
#Therefore, you need to copy the code to the required leetcode question solution section to verify it. After selecting Python3, copy it to the answer section.