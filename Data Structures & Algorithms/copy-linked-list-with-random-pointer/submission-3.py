"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # Step 1: Create a Copy right next to the current nodes
        l1 = head
        while l1:
            l2 = Node(l1.val, l1.next)
            l1.next = l2
            l1 = l2.next
        
        # Step 2: update l2's randoms
        l1 = head
        while l1:
            if l1.random:
                # Since we created the deep copy after each node, we know it is at next of the random
                l1.next.random = l1.random.next
            l1 = l1.next.next # Jump 2
        
        newHead = head.next # Save since we are separating
        
        # Step 3 separate
        l1 = head
        while l1: # Separate two lists
            l2 = l1.next
            l1.next = l2.next
            if l2.next:
                l2.next = l2.next.next # Jump 2 again due to alternating
            l1 = l1.next
        
        return newHead
            