class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = ""
        first_row_dist = max(1, 2 * (numRows - 1))
        for i in range(numRows):
            for pos, symb in enumerate(s):
                if (pos + i) % first_row_dist == 0 or (pos - i) % first_row_dist == 0:
                    result = result + symb
        return result

#This part only contains the solution. The codes may not work directly.
#Therefore, you need to copy the code to the required leetcode question solution section to verify it. After selecting Python3, copy it to the answer section.