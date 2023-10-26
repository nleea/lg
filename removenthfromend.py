# Definition for singly-linked list.
from pyparsing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self) -> None:
        self.array = []
        

    def createNode(self):
        temp = None

        for i in self.array[::-1]:
            if temp == None:
                temp = ListNode(i)
            else:
                node = ListNode(i)
                node.next = temp
                temp = node
        return temp

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node = head
        index = 0

        while node:
            
            self.array.append(node.val)
            index += 1
            node = node.next

        self.array.pop(index - n)

        return self.createNode()


temp = None

for i in [1,2,3,4,5]:
    if temp == None:
        temp = ListNode(i)
    else:
        node = ListNode(i)
        node.next = temp
        temp = node


s = Solution()
a = s.removeNthFromEnd(temp,2)

while a:
    print(a.val)
    
    a = a.next