class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

def detectLoop(head):
    st = set()

    while head is not None:

        # if this node is already present
        # in hashmap it means there is a cycle
        if head in st:
            return True

        # if we are seeing the node for
        # the first time, insert it in hash
        st.add(head)

        head = head.next

    return False

if __name__ == "__main__":

    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(4)

    head.next.next.next = head.next

    if detectLoop(head):
        print("true")
    else:
        print("false")