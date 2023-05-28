"""
https://contest.yandex.ru/contest/23815/submits/?success=87719027
ПРИНЦИП РАБОТЫ
Алгоритм поиска в сломанном кольцевом буфере работает следующим образом:
1. Сначала вызываем бинарный поиск для нахождения индекса максимального элемента в списке.
Изначально за максимальный элемент принимаем элемент с индексом 0. Затем до тех пор, пока левый и правый указатели
не встретятся осуществляем поиск, по окончанию получаем индекс максимального элемента.
2. Имея информацию о значении искомого элемента вызываем обычный бинарный поиск для правой или левой части списка.


ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ
Из описания алгоритма следует, что алгоритм при помощи бинарного поиска ищет переломный элемент, а затем выполняет классический бинарный
поиск в части, расположенной до него,  либо в части, расположенной после.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Алгоритм использует до трех последовательных вызовов бинарного поиска, при этом следующая часть предположительно меньше предыдущей.
В худшем случае алгоритм работает за O(log N)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Список содержит N объектов, занимает O(N) памяти, дополнительно мы используем О(1) памяти для хранения индексов.
Поэтому мой алгоритм будет требовать O(N) * O(1) = O(N) памяти.
"""


def broken_search(nums, target) -> int:
    def search_max(arr, left, right):
        while right - left > 1:
            mid = (right + left) // 2
            if arr[mid] < arr[right]:
                right = mid
            elif arr[mid] > arr[left]:
                left = mid
            else:
                assert False
        return left if arr[left] >= arr[right] else right

    if len(nums) > 1:
        max_idx = search_max(nums, left=0, right=len(nums) - 1)
    else:
        max_idx = 0

    def binary_search(arr, x, left, right):
        while right - left > 1:
            mid = (right + left) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                left = mid
            elif arr[mid] > x:
                right = mid
        for i in (left, right):
            if arr[i] == x:
                return i
        return -1

    if (target >= nums[0]) and (target <= nums[max_idx]):
        index = binary_search(nums, target, left=0, right=max_idx)
    elif target <= nums[len(nums) - 1]:
        index = binary_search(nums, target, left=max_idx + 1, right=len(nums) - 1)
    else:
        return -1
    return index


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
