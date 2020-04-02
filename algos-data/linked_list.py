class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list!")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node


if __name__ == "__main__":
    llist = LinkedList()

    llist.append("Cube")
    llist.append("Tesseract")
    llist.append("Spinor")
    llist.append("Hopf Fibration")
    llist.prepend("lol")

    # print(llist.head.data)
    # print(llist.head.next.data)
    # print(llist.head.next.next.data)

    llist.insert_after_node(llist.head, "lmfao")
    llist.insert_after_node(llist.head.next, "rofl")
    llist.print_list()
