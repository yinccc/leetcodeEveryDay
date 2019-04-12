class Solution:
    def reverseLinkedList(self,head):
        curr=head
        prev=None

        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next

        return prev

class LinkedList:
    def __init__(self,val):
        self.val=val
        self.next=None


a=LinkedList(1)
b=LinkedList(2)
c=LinkedList(3)
d=LinkedList(4)
e=LinkedList(5)

a.next=b
b.next=c
c.next=d
d.next=e
S=Solution()
print(S.reverseLinkedList(a).val)
