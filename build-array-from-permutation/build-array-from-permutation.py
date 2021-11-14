class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        output = []
        for x in range(len(nums)):
            output.insert(x, nums[nums[x]])
        return output