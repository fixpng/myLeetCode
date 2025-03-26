# 234. 回文链表
"""
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
"""

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        val=[]
        while head is not None:
            val.append(head.val)
            head = head.next
        return val == val[::-1]


# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Test case
head = create_linked_list([1, 2, 2, 1])  # Convert
print(head.next.val)
print(Solution().isPalindrome(head)) # True