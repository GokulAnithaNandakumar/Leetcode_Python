# I didn't do this question
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        h=head
        x=0
        while h:
            h=h.next
            x+=1
        f=1
        if(x%2==0):
            while f<x/2+1:
                f=f+1
                head=head.next
            return head
        else:
            while f<int(x/2)+1:
                f=f+1
                head=head.next
            return head