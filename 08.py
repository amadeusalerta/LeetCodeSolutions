class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
    
        if len(s) == 0:
            return 0
    
        if s[0] == '-' or s[0] == '+':
            sign = -1 if s[0] == '-' else 1
            s = s[1:]  
        else:
            sign = 1

        digits = []
        for c in s:
            if c.isdigit():
                digits.append(c)
            else:
                break
    
    # convert digits to an integer
        if len(digits) == 0:
            return 0
        else:
            num = int(''.join(digits))
            num *= sign
    
    # clamp the integer to the range [-2**31, 2**31 - 1]
        num = max(num, -2**31)
        num = min(num, 2**31 - 1)
    
        return num

#This part only contains the solution. The codes may not work directly.
#Therefore, you need to copy the code to the required leetcode question solution section to verify it. After selecting Python3, copy it to the answer section.