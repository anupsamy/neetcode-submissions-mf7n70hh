class Solution:
    def reverse(self, x: int) -> int:
        temp = x
        x = abs(x)
        res = int(str(x)[::-1])

        if temp < 0:
            res = res * -1
        
        if -2**31 > res or res > 2**31 - 1:
            return 0

        return res
        