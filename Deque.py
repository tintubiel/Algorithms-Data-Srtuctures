"""
https://contest.yandex.ru/contest/22781/submits/

ПРИНЦИП РАБОТЫ
Дек, используемый в программе, реализован на массиве фиксированного размера.
Реализация Дека подразумевает следующие операции:
1. Добавление и удаление элемента из головы
2. Добавление и удаление из хвоста

В начальный момент времени и голова и хвост указывают на индекс 0. Далее мы рассматриваем изменение индексации
согласно концепции кольцевого буфера.
1) При добавлении элемента в хвост происходит смещение указателя tail на +1, а также увеличение размера дека на +1.
2) При добавлении элемента в голову происходит смещение указателя head на -1, а также увеличение размера дека на +1.
3) При удалении элемента из хвоста значение на позиции tail-1 обращается в None,
указатель tail сдвигается на -1 и размер дека уменьшается на 1
4) При удалении элемента из головы значение на позиции head обращается в None,
указатель на head сдвигается на +1 и размер дека уменьшается на 1

ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ
Из описания алгоритма следует, что при условии заранее заданного размера дека, мы реализовали дек, основанный на массиве.
В котором реализованы операции добавления и уаления элементов в хвост и голову.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Добавление в дек и в голову, и в хвост стоит O(1).
Удаление из дека из головы, и из хвоста также стоит О(1)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Дек, с максимальной емкостью N элементов, занимает O(N) памяти, вне зависимости от того, сколько из них содержательных.

"""

import sys


class Deque:
    def __init__(self, max_n):
        self.deque = [None] * max_n
        self.max_n = max_n
        self.head = 0
        self.tail = 0
        self.size = 0

    def push_back(self, x):
        if self.size != self.max_n:
            self.deque[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print("error")

    def push_front(self, x):
        if self.size != self.max_n:
            self.head = (self.head - 1 + self.max_n) % self.max_n
            self.deque[self.head] = x
            self.size += 1
        else:
            print("error")

    def pop_back(self):
        if self.size == 0:
            print("error")
        else:
            self.tail = (self.tail - 1 + self.max_n) % self.max_n
            print(self.deque[self.tail])
            self.deque[self.tail] = None
            self.size -= 1

    def pop_front(self):
        if self.size == 0:
            print("error")
        else:
            print(self.deque[self.head])
            self.deque[self.head] = None
            self.head = (self.head + 1) % self.max_n
            self.size -= 1


def main():
    n = int(sys.stdin.readline().rstrip())
    max_size = int(sys.stdin.readline().rstrip())
    new_deque = Deque(max_n = max_size)
    for i in range(n):
        line = sys.stdin.readline().rstrip()
        line_list = line.split()
        if len(line_list) > 1:
            function = getattr(new_deque, line_list[0])
            function(int(line_list[1]))
        else:
            function = getattr(new_deque, line_list[0])
            function()


if __name__ == '__main__':
    main()
