import sys


def merge_sort(arr):
    if len(arr) < 2:
        return
    temp = [None] * len(arr)
    merge_sort_helper(arr, temp, 0, len(arr) - 1)


def merge_sort_helper(arr, temp, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort_helper(arr, temp, left, mid)
        merge_sort_helper(arr, temp, mid + 1, right)
        merge(arr, temp, left, mid, right)


def merge(arr, temp, left, mid, right):
    i = left  # Индекс для левой половины
    j = mid + 1  # Индекс для правой половины
    k = left  # Индекс для временного списка

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1
    for index in range(left, right + 1):
        arr[index] = temp[index]


def main():
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        arr = sys.stdin.readline().rstrip().split(" ")
        print(" ")
    else:
        arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
        merge_sort(arr)
        print(" ".join(map(str, arr)))

main()
