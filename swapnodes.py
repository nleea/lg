# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def generate(self,array):
        temp = None
        for i in array:
            if temp == None:
                temp = ListNode(i)
            else:
                node = ListNode(i)
                node.next = temp
                temp = node
        return temp

    def swapPairs(self, head: ListNode) -> ListNode:
        temp = head
        i = 1
        array = []

        while temp:

            if i == 2:
                array.insert(len(array)-1,temp.val)
                i = 1
                temp = temp.next
                continue

            array.append(temp.val)
            temp = temp.next
            i = 2

        return self.generate(array[::-1])



temp = None

for i in [1,2,3,4]:
    if temp == None:
        temp = ListNode(i)
    else:
        node = ListNode(i)
        node.next = temp
        temp = node

s = Solution()
a = s.swapPairs(temp)

while a:
    print(a.val)
    a = a.next

