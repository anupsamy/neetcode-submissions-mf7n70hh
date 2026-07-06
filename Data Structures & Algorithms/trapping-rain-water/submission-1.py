class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]
        totalWater = 0

        while l < r:
            if maxLeft < maxRight:
                l+= 1
                maxLeft = max(maxLeft, height[l])
                totalWater += max(min(maxLeft, maxRight) - height[l], 0)
            else:
                r-= 1
                maxRight = max(maxRight, height[r])
                totalWater += max(min(maxLeft, maxRight) - height[r], 0)
            
        return totalWater
        