class Solution(object):
    def longestPalindrome(self,s):
        leng, number1, number2 = len(s), 0, 1
        
        for i in range(leng):
            for alpha,beta in (i, i), (i, i+1):
                while 0 <= alpha and beta < leng and s[alpha] == s[beta]: 
                    alpha,beta = alpha-1, beta+1
                if beta-alpha > number2-number1: 
                    number1, number2 = alpha+1, beta
        
        return s[number1:number2]
    
#This part only contains the solution. The codes may not work directly.
#Therefore, you need to copy the code to the required leetcode question solution section to verify it. After selecting Python3, copy it to the answer section.