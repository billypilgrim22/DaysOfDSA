class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        19. Remove Nth Node From End of List: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

        1. Get the total length of the LL by traversing till end.
        2. Subtract n from total length to find position of node to be removed.
        3. Traverse till the node right before that position.
        4. Point that node to it's .next.next!
        '''
        list_length = 0
        temp = head
        while(temp):
            temp = temp.next
            list_length += 1
        loc = list_length - n
        if(loc == 0):
            head = head.next
            return head
        temp = head
        while(loc>1):
            temp = temp.next
            loc -=1
        temp.next = temp.next.next
        return head