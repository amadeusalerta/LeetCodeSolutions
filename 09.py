class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        if str(x) == (str(x)[::-1]):
            return True

#This part only contains the solution. The codes may not work directly.
#Therefore, you need to copy the code to the required leetcode question solution section to verify it. After selecting Python3, copy it to the answer section.