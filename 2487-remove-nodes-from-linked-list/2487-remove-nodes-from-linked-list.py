# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = list()
        temp = head
        
        while temp:
            arr.append(temp.val)
            temp = temp.next
        
        stack = [-1]
        
        for val in arr:
            while stack and val > stack[-1]:
                stack.pop()
            stack.append(val)
        
        head = ListNode(stack[0])
        temp = head
        
        for i in range(1, len(stack)):
            x = stack[i]
            node = ListNode(x)
            temp.next = node
            temp = temp.next
            
        
        return head
            
        
            
        
        
            
        
        