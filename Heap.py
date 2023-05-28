import sys
#import time


class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, num):
        self.heap.append(num)
        child = len(self.heap) - 1
        parent = self._parent(child)
        while parent > 0:
            if self.heap[parent] < self.heap[child]:
                self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
            child = parent
            parent = self._parent(child)

        if self.heap[parent] < self.heap[child]:
            self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]

    def extract(self):
        deleted = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        parent = 0
        left_child = 2 * parent + 1
        right_child = left_child + 1
        while left_child < len(self.heap) and right_child < len(self.heap):
            if self.heap[left_child] > self.heap[right_child]:
                child = left_child
            else:
                child = right_child

            if self.heap[parent] < self.heap[child]:
                self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
            parent = child
            left_child = 2 * parent + 1
            right_child = left_child + 1

        if right_child >= len(self.heap):
            if left_child < len(self.heap):
                if self.heap[parent] < self.heap[left_child]:
                    self.heap[parent], self.heap[left_child] = self.heap[left_child], self.heap[parent]
        return deleted

    @staticmethod
    def _parent(index: int) -> int:
        return (index - 1) // 2


def main():
    new_heap = Heap()

    n = int(sys.stdin.readline().rstrip())
    i = 0
    #start = time.time()
    while i < n:
        line = sys.stdin.readline().rstrip()
        if line[0] == "0":
            line_list = line.split()
            new_heap.insert(int(line_list[1]))
        else:
            print(new_heap.extract())
        i += 1

    #end = time.time() - start
    #print(end)


# def test(array: list[int]):
#     new_heap = Heap()
#     for x in array:
#         new_heap.insert(x)
#
#     print(new_heap.heap)
#
#     for i in range(len(array)):
#         print(new_heap.extract())
#         print(new_heap.heap)



if __name__ == '__main__':
    main()
