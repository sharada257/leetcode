# @leetsync-header
# Problem: 2. Add Two Numbers (Medium)
# Language: Python3
# Runtime: 3 ms (Beats 65.41%)
# Memory: 19.2 MB (Beats 79.76%)
# Submission: https://leetcode.com/problems/add-two-numbers/submissions/2157918270/
# Submitted: 2026-09-30T07:24:05.657Z

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        temp=dummy
        rem=0
        while(l1 or l2 or rem):
            val1= l1.val if l1 else 0
            val2= l2.val if l2 else 0
            sum=val1+val2+rem
            value=sum%10
            rem=sum//10
            temp.next=ListNode(value)
            temp=temp.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return dummy.next
