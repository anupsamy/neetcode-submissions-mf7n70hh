class Solution:
    def mySqrt(self, x: int) -> int:
        root = math.sqrt(x)
        root = math.floor(root)

        return root