class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


# Function to merge only 2 lists
def mergeTwo(head1, head2):
    # Create a dummy node to simplify
    # the merging process
    dummy = Node(-1)
    curr = dummy

    # Iterate through both linked lists
    while head1 is not None and head2 is not None:

        # Add the smaller node to the merged list
        if head1.data <= head2.data:
            curr.next = head1
            head1 = head1.next
        else:
            curr.next = head2
            head2 = head2.next
        curr = curr.next

    # If any list is left, append it to
    # the merged list
    if head1 is not None:
        curr.next = head1
    else:
        curr.next = head2

    # Return the merged list starting
    # from the next of dummy node
    return dummy.next


# Function to merge K sorted linked lists
def mergeKLists(arr):
    # Initialize result as empty
    res = None

    # One by one merge all lists with
    # res and keep updating res
    for node in arr:
        res = mergeTwo(res, node)

    return res


def printList(node):
    while node is not None:
        print(f"{node.data}", end="")
        if node.next is not None:
            print(" -> ", end="")
        node = node.next
    print()


if __name__ == "__main__":
    arr = []

    node1 = Node(1)
    node1.next = Node(3)
    node1.next.next = Node(5)
    node1.next.next.next = Node(7)
    arr.append(node1)

    node2 = Node(2)
    node2.next = Node(4)
    node2.next.next = Node(6)
    node2.next.next.next = Node(8)
    arr.append(node2)

    node3 = Node(0)
    node3.next = Node(9)
    node3.next.next = Node(10)
    node3.next.next.next = Node(11)
    arr.append(node3)

    head = mergeKLists(arr)
    printList(head)