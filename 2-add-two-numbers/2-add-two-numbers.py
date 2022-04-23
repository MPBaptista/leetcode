# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:        
        reversed_l1 = (self.convert_linked_list_to_string(l1, ""))[::-1]
        reversed_l2 = (self.convert_linked_list_to_string(l2, ""))[::-1]
        
        sum_reversed = str(int(reversed_l1) + int(reversed_l2))[::-1]
        
        return self.convert_string_to_linked_list(sum_reversed)
        
        
    def convert_linked_list_to_string(self, list_node: ListNode, number_string: str) -> str:
        # Using recursion
        number_string += str(list_node.val) 
        if list_node.next is not None:
            return self.convert_linked_list_to_string(list_node.next, number_string)
        else:
            return number_string
        
    def convert_string_to_linked_list(self, number_list: str) -> [ListNode]:
        # Using iteration
        previousNode = None
        first = None
        for i in number_list:
            currentNode = ListNode(i)
            if first is None:
                first = currentNode
            if previousNode is not None:
                previousNode.next = currentNode
            previousNode = currentNode
        return first
            
            