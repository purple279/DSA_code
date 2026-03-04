class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def reverse(head):
        prev = None
        current = head

        while current is not None:
            next_node = current.next # store next
            current.next = prev      # reverse pointer
            prev = current           # move prev forward
            current = next_node      # move current forward

        return prev    # new head
