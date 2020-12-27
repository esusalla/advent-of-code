# Day 23, Part 2: Crab Cups


class LList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_back(self, data):
        node = self.Node(data)
        if not self.head:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next_node = node
            node.prev_node = self.tail
            self.tail = node

        return node

    def connect(self):
        self.head.prev_node = self.tail
        self.tail.next_node = self.head

    class Node:
        def __init__(self, data):
            self.data = data
            self.next_node = None
            self.prev_node = None


def shuffle(current, cups, nodes):
    rmv_start = nodes[current].next_node
    rmv_end = rmv_start

    # Remove three cups after current cup
    removed = []
    for _ in range(3):
        removed.append(rmv_end.data)
        rmv_end = rmv_end.next_node
    rmv_end = rmv_end.prev_node

    # Relink current cup to the cup following the last of the three removed
    nodes[current].next_node = rmv_end.next_node
    nodes[current].next_node.prev_node = nodes[current]

    # Calculate insertion destination for removed cups by subtracting
    # from current cup until its value is not included in the removed cups.
    # Circle back to max cup upon reaching zero
    destination = LIMIT if current - 1 == 0 else current - 1
    while destination in removed:
        destination = LIMIT if destination - 1 == 0 else destination - 1

    # Reinsert the three removed cups after the destination cup and relink
    rmv_start.prev_node = nodes[destination]
    rmv_end.next_node = nodes[destination].next_node

    nodes[destination].next_node.prev_node = rmv_end
    nodes[destination].next_node = rmv_start

    # Return the cup immediately after the current one
    return nodes[current].next_node.data


if __name__ == "__main__":
    START = [int(n) for n in "364297581"]  # input
    LIMIT = 1000000
    ROUNDS = 10000000

    cups = LList()
    nodes = [0 for _ in range(LIMIT + 1)]

    # Insert input as array start
    for n in START:
        nodes[n] = cups.push_back(n)

    # Fill rest of array with ascending numbers to limit
    for n in range(len(START) + 1, LIMIT + 1):
        nodes[n] = cups.push_back(n)

    # Connect the head and tail of the array to make circular iterations easier
    cups.connect()

    current = cups.head.data
    for _ in range(ROUNDS):
        current = shuffle(current, cups, nodes)

    # Calculate product of two cups immediately following number one
    prod = nodes[1].next_node.data * nodes[1].next_node.next_node.data
    print(prod)
