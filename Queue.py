import sys


class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next = next_item


class Queue:
    def __init__(self, max_n=None, tail_node=None, head_node=None):
        self.size = 0
        self.max_n = max_n
        self.head = head_node
        self.tail = tail_node

    def put(self, value):
        new_node = Node(value)
        if self.size == self.max_n:
            print("error")
        else:
            if self.size == 0:
                self.head = new_node
                self.tail = new_node
            elif self.size < self.max_n:
                prev_node = self.head
                self.head = new_node
                prev_node.next = self.head
            self.size += 1

    def pop(self):
        if self.size == 0:
            print("None")
        else:
            print(self.tail.value)
            self.tail.value = None
            self.tail = self.tail.next
            self.size -= 1

    def peek(self):
        if self.size == 0:
            return "None"
        else:
            return self.tail.value

    def get(self):
        if self.size == 0:
            return "error"
        else:
            value = self.tail.value
            self.pop()
            return value

    def size_of(self):
        return self.size


def main():
    new_queue = Queue()
    n = int(sys.stdin.readline().rstrip())
    max_size = int(sys.stdin.readline().rstrip())
    new_queue.max_n = max_size
    for i in range(n):
        line = sys.stdin.readline().rstrip()
        line_list = line.split()
        if line_list[0] == "push":
            new_queue.push(line_list[1])
        elif line_list[0] == "pop":
            new_queue.pop()
        elif line_list[0] == "peek":
            print(new_queue.peek())
        elif line_list[0] == "size":
            print(new_queue.size_of())


if __name__ == '__main__':
    main()
