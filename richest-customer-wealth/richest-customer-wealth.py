class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        highest_wealth = 0
        for account in accounts:
            if sum(account) > highest_wealth:
                highest_wealth = sum(account)
        return highest_wealth
        