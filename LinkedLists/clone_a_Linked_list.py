class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.random = None


def cloneLinkedList(head):
    nodeMap = {}
    curr = head

    # Traverse original linked list to store new nodes
    # corresponding to original linked list
    while curr is not None:
        nodeMap[curr] = Node(curr.data)
        curr = curr.next

    curr = head

    # Loop to update the next and random pointers
    # of new nodes
    while curr is not None:
        newNode = nodeMap[curr]

        newNode.next = nodeMap.get(curr.next)

        newNode.random = nodeMap.get(curr.random)
        curr = curr.next

    return nodeMap.get(head)


def printList(head):
    curr = head
    while curr is not None:
        print(f'{curr.data}(', end='')
        if curr.random:
            print(f'{curr.random.data})', end='')
        else:
            print('null)', end='')

        if curr.next is not None:
            print(' -> ', end='')
        curr = curr.next
    print()


if __name__ == "__main__":
    # Creating a linked list with random pointer
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    head.random = head.next.next
    head.next.random = head
    head.next.next.random = head.next.next.next.next
    head.next.next.next.random = head.next.next
    head.next.next.next.next.random = head.next

    # Print the original list
    print("Original linked list:")
    printList(head)

    clonedList = cloneLinkedList(head)

    print("Cloned linked list:")
    printList(clonedList)