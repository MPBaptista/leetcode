class Solution:
    def isValid(self, input_str: str) -> bool:
        stack = []
        char_dict = {"[":"]", "(":")", "{":"}"}
        
        for char in input_str:
            if char in char_dict:
                stack.append(char)
            elif stack == [] or char_dict[stack.pop()] != char:
                return False
        return len(stack) == 0