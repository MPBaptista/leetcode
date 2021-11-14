class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            # iterate over list to find first element of pair
            for x in range(len(nums)-1):
                # iterate over list from x+1 to find second element of pair
                for y in range(x+1, len(nums)):
                    # if sum matches target return list with indexes
                    if nums[x] + nums[y] == target:
                        return [x, y]
        