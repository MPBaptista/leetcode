class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        highest = max(candies)
        output = []
        for element in candies:
            if element + extraCandies >= highest:
                output.append(True)
            else:
                output.append(False)
        return output
            
