class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        output = []
        for x in nums:
            sum += x
            output.append(sum)
        return output
            
            