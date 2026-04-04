class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            a = nums[i]
            if a > 0:
                break
            
            #skip duplicates in a
            if i > 0 and a == nums[i - 1]:
                continue

            l =  i + 1
            r = len(nums) - 1
            while l < r:
                sums = a + nums[l] + nums[r]
                if sums == 0:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l+= 1
                elif sums > 0:
                    r -= 1
                else:
                    l += 1

        return res
