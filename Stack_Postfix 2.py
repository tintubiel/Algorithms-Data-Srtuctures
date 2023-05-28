"""
https://contest.yandex.ru/contest/22781/run-report/82421454/

ПРИНЦИП РАБОТЫ
Стек, используемый в программе, реализован на односвязном списке.
Калькулятор для постфиксной записи работает следующим образом:
1. После преобразования строки получаем массив из целых чисеал и знаков
2. В цикле идем по массиву, если встречаем число - кладем его в стек, если встречаем знак -
достаем два последних числа из стека и применяем к ним соответствующую операцию.
Результат операции кладем в стек.
3. При достижении конца списка в стеке лежит результат применения всех операций

ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ
Из описания алгоритма следует, что чем дальше располагается от начала строки знак, тем позже
мы должны произвести соответствующую ему арифметическую операцию. Соответственно в стеке
накапливаются промежуточные результаты вычислений калькулятора, а итоговый результат окажется
единственным элементом в стеке.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Добавление в стек стоит O(1).
Удаление из стека также стоит О(1)

В строке длиной N есть K чисел и К-1 знаков. Итоговая работа функции калькулятора не превышает
сложности О(2*K + 2*K/2) + О(К-1) = О(K)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Строка содержит N элементов, занимает O(N) памяти.
Стек, содержащий K элементов, занимает O(K) памяти.
Поэтому мой алгоритм будет требовать O(N) + O(K) = O(N) памяти.
"""


import sys


class Node:
    def __init__(self, value, prev_item=None):
        self.value = value
        self.prev = prev_item


class Stack:
    def __init__(self, head_node=None):
        self.size = 0
        self.head = head_node

    def push(self, value):
        new_node = Node(value)
        if self.size == 0:
            self.head = new_node
        else:
            prev_node = self.head
            self.head = new_node
            new_node.prev = prev_node
        self.size += 1

    def pop(self):
        if self.size == 0:
            print("error")
        else:
            value = self.head.value
            self.head = self.head.prev
            self.size -= 1
            return value

    def size_of(self):
        return self.size


def main():
    operation = {"+": lambda y, x: x + y,
                 "-": lambda y, x: x - y,
                 "*": lambda y, x: x * y,
                 "/": lambda y, x: x // y}
    new_stack = Stack()
    line = sys.stdin.readline().rstrip()
    line_list = line.split()
    for i in range(len(line_list)):
        if line_list[i] in ["*", "+", "/", "-"]:
            new_stack.push(operation[line_list[i]](new_stack.pop(), new_stack.pop()))
        else:
            new_stack.push(int(line_list[i]))
    print(new_stack.head.value)


if __name__ == '__main__':
    main()
