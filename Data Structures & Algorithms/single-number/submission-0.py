class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unseen = set()

        for i in nums:
            if i in unseen:
                unseen.remove(i)
            else:
                unseen.add(i)
        
        return unseen.pop()