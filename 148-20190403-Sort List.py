class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None



class Solution:
    def Sortlist(self,head):
        if not head or not head.next:
            return head
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        slow.next=None
        l1=self.Sortlist(head)
        l2=self.Sortlist(second)
        return self.merge(l1,l2)

    def merge(self,l1,l2):
        dummy=cur=ListNode(0)
        while l1 and l2:
            if l1.val<l2.val:
                cur.next=l1
                l1=l1.next
            else:
                cur.next=l2
                l2=l2.next
            cur=cur.next
        cur.next=l1 or l2
        return dummy.next

a=ListNode(0)
b=ListNode(3)
c=ListNode(1)
d=ListNode(9)

a.next=b
b.next=c
c.next=d
S=Solution()
print(S.Sortlist(a).val)
print(S.Sortlist(a).next.val)
print(S.Sortlist(a).next.next.val)
print(S.Sortlist(a).next.next.next.val)