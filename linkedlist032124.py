def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        
        while current:
            next_node = current.next # Save the next node
            current.next = prev # Reverse the link
            prev = current # Move pointers one position ahead
            current = next_node
        
        # 'prev' now points to the new head of the reversed list
        return prev
