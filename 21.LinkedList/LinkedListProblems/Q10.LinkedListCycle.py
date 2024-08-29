class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

    def hasCycle(self, head) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
