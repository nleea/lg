class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        tail = slow.next
        slow.next = None

        prev = None
        curr = tail
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        head1 = head
        head2 = prev
        while head1 and head2:
            next1 = head1.next
            next2 = head2.next

            head1.next = head2
            head2.next = next1

            head1 = next1
            head2 = next2

        return head


temp = None

for i in [1, 2, 3, 4, 5][::-1]:
    if temp == None:
        temp = ListNode(i)
        continue
    node = ListNode(i)
    node.next = temp
    temp = node

s = Solution()
s.reorderList(temp)

while temp:
    print(temp.val)
    temp = temp.next
