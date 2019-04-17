class LinkedList:
    def __init__(self,val):
        self.val=val
        self.next=None

class Solution:
    def PalindromLinkedList(self,head):
        fast=head
        slow=head
        prev=None
        while fast and fast.next:
            fast=fast.next.next
            prev,prev.next,slow=slow,prev,slow.next
        if fast:
            slow=slow.next
        while prev and slow.val==prev.val:
            slow=slow.next
            prev=prev.next
        return not prev

a=LinkedList(1)
b=LinkedList(2)
c=LinkedList(3)
d=LinkedList(3)
e=LinkedList(2)
f=LinkedList(1)
a.next=b
b.next=c
c.next=d
d.next=e
#e.next=f

S=Solution()
print(S.PalindromLinkedList(a))