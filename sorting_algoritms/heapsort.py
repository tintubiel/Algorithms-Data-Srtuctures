import sys


def does_exist(index, size):
    return index < size


def heapify(heap, break_inx, size):
    parent = break_inx
    left_child = 2 * parent + 1
    right_child = left_child + 1
    while does_exist(left_child, size) and does_exist(right_child, size):
        if heap[left_child] > heap[right_child]:
            child = left_child
        else:
            child = right_child

        if heap[parent] < heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        left_child = 2 * parent + 1
        right_child = left_child + 1

    if right_child >= size:
        if left_child < size:
            if heap[parent] < heap[left_child]:
                heap[parent], heap[left_child] = heap[left_child], heap[parent]



def extract(heap, size):
    deleted = heap[0]
    heap[0] = heap[size - 1]
    heap[size - 1] = deleted


def sort(heap, n):
    size = n
    for i in reversed(range(n)):
        parent = i
        left_child = 2 * parent + 1
        right_child = left_child + 1
        if does_exist(left_child, size):
            heapify(heap, i, n)

    while size > 0:
        extract(heap, size)
        size -= 1
        if size >= 1:
            heapify(heap, 0, size)

    return heap


def main():
    n = int(sys.stdin.readline().rstrip())
    line = sys.stdin.readline().rstrip()
    heap = list(map(int, line.split()))
    print(*sort(heap, n))


# def test():
#     # 6
#     # 3 4 6 2 6 7


if __name__ == '__main__':
    main()
