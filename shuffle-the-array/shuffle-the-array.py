class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first_list = []
        second_list = []
        output = []
        for x in range(len(nums)):
            if x < n:
                first_list.append(nums[x])
            else:
                second_list.append(nums[x])
        
        for x in range(n):
            output.append(first_list[x])
            output.append(second_list[x])
            
        return output
                
            