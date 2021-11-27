class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        kidsCandySum = []
        output = []
        greatest = 0
        for x in candies:
            kidsCandySum.append(x + extraCandies)
            if x > greatest:
                greatest = x
        for y in kidsCandySum:
            if y >= greatest:
                output.append(True)
            if y < greatest:
                output.append(False)
                
        return output
            