class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Insert copied nodes after original nodes
        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next

        # Step 2: Assign random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Separate the original and copied lists
        curr = head
        dummy = Node(0)
        copy_curr = dummy

        while curr:
            copy = curr.next
            curr.next = copy.next

            copy_curr.next = copy
            copy_curr = copy

            curr = curr.next

        return dummy.next