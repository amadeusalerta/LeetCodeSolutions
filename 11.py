class Solution:
    def maxArea(self, li: List[int]) -> int:
        line_lenght = 0
        point_01 = 0
        point_02 = len(li) - 1

        while point_01 < point_02:
            diff = point_02 - point_01
            length = min(li[point_01], li[point_02])
            line_lenght = max(line_lenght, diff * length)

            if li[point_01] < li[point_02]:
                point_01 += 1
            else:
                point_02 -= 1

        return line_lenght
    
#This part only contains the solution. The codes may not work directly.
#Therefore, you need to copy the code to the required leetcode question solution section to verify it. After selecting Python3, copy it to the answer section.