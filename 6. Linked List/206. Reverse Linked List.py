from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            tempnext = curr.next
            curr.next = prev
            prev = curr
            curr = tempnext
        return prev


testInputs = [
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
    ListNode(1, ListNode(2)),
    None,
]
for head in testInputs:
    reversed_head = Solution().reverseList(head)
    if reversed_head:
        while reversed_head:
            print(reversed_head.val, end=" -> ")
            reversed_head = reversed_head.next
        print("None")
    else:
        print("Empty List")
