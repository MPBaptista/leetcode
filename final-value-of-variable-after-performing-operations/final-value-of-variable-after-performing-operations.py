class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        output_value = 0
        subtract_operations = ["--X", "X--"]
        add_operations = ["++X", "X++"]
        for x in operations:
            if x in add_operations:
                output_value += 1
            if x in subtract_operations:
                output_value -= 1
        return output_value