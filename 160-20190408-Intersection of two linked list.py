class Solution:
    def intersectionOftwoLinkedList(self,headA,headB):
        if headA is None or headB is None:
            return None
        pa=headA
        pb=headB
        while pa is not pb:
            pa=headB if pa is None else pa.next
            pb=headA if pb is None else pb.next

        return pb

class Linklist:
    def __init__(self,val):
        self.next=None
        self.val=val


a=Linklist(1)
b=Linklist(2)
c=Linklist(3)
d=Linklist(4)
e=Linklist(5)

a.next=b
b.next=c
d.next=c
c.next=e

S=Solution()
print(S.intersectionOftwoLinkedList(a,d).val)