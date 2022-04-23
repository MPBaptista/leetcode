class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ""
        shortest_string = min(strs, key=len)
        
        for i in range(len(shortest_string)):
            if all([string.startswith(shortest_string[:i+1]) for string in strs]):
                longest_prefix = shortest_string[:i+1]
            else:
                break
        
        return longest_prefix
        