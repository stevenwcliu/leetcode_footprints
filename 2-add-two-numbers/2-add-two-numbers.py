# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#             # 1) Create a dummy head. This will be our reference to our return list.
#             dummyHead = ListNode()
#             # 3) Create a curr pointer that helps us build the return list
#             cur = dummyHead

#             # 4) Initialize a variable to store the carry value, if any, as we compute the sum. 
#             carry = 0
#             # 5) Traverse the two lists while our two pointers are not null
#             # or carry: catch the edge case
#             while l1 or l2 or carry:
#                 # a) Find the values at each pointer
#                 v1 = l1.val if l1 else 0
#                 v2 = l2.val if l2 else 0

#                 # b) Find and store their sum
#                 sum = v1 + v2 + carry
#                 carry = sum // 10 # !! 
#                 val = sum % 10 # !!
#                 cur.next = ListNode(val)

#                 # update ptrs
#                 cur = cur.next
#                 # alternate 
#                 # if l1 != None:
#                 #     l1 = l1.next;
#                 # if l2 != None:
#                 #     l2 = l2.next;
#                 l1 = l1.next if l1 else None
#                 l2 = l2.next if l2 else None

#             return dummyHead.next
            
            dummyHead = ListNode() # reference to the return list
            cur = dummyHead
            
            carry = 0
            
            while l1 or l2 or carry:
                v1 = l1.val if l1 else 0
                v2 = l2.val if l2 else 0
                
                sum = v1 + v2 + carry
                # keypoints
                carry = sum // 10 # 12 // 10 -> 1
                val = sum % 10 # 12 % 10 -> 2
                cur.next = ListNode(val)
                
                cur = cur.next
                l1 = l1.next if l1 else None
                l2 = l2.next if l2 else None
                
            return dummyHead.next # head of the return ll