# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseEvenLengthGroups(self, head):
        dummy = ListNode(0, head)
        prev_group_tail = dummy
        group_size = 1

        while prev_group_tail.next:
            # Find the actual length of the current group
            count = 0
            node = prev_group_tail.next
            while node and count < group_size:
                node = node.next
                count += 1

            # Reverse if the group's actual length is even
            if count % 2 == 0:
                prev = node
                curr = prev_group_tail.next
                for _ in range(count):
                    nxt = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nxt

                new_group_tail = prev_group_tail.next
                prev_group_tail.next = prev
                prev_group_tail = new_group_tail
            else:
                for _ in range(count):
                    prev_group_tail = prev_group_tail.next

            group_size += 1

        return dummy.next
