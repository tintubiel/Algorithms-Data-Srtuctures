import sys


class Node:
    def __init__(self, value, index,  prev_item=None):
        self.value = value
        self.index = index
        self.prev = prev_item


class Stack:
    def __init__(self, head_node=None):
        self.size = 0
        self.head = head_node

    def push(self, value, index):
        new_node = Node(value,index)
        if self.size == 0:
            self.head = new_node
        else:
            prev_node = self.head
            self.head = new_node
            new_node.prev = prev_node
        self.size += 1

    def pop(self):
        if self.size != 0:
            self.head = self.head.prev
            self.size -= 1


def main():
    new_stack = Stack()
    n = int(sys.stdin.readline().rstrip())
    line = sys.stdin.readline().rstrip()
    answer = [-1] * n

    def low_cost_idx(line):
        list_line = list(map(int, line.split()))
        for i in range(n):
            if new_stack.size == 0:
                new_stack.push(list_line[i], i)
            elif list_line[i] < new_stack.head.value:

                while new_stack.head.value > list_line[i]:
                    answer[new_stack.head.index] = i
                    new_stack.pop()
                    if new_stack.size == 0:
                        break
            new_stack.push(list_line[i], i)
        return answer

    print(* low_cost_idx(line))



if __name__ == '__main__':
    main()
