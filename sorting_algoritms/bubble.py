import sys

def bubble_sort(line_list, n):
    for j in range(n-1):
        flag = 0
        for i in range(n-1):
            if line_list[i] > line_list[i+1]:
                flag = 1
                line_list[i], line_list[i+1] = line_list[i+1], line_list[i]
        if flag == 0 and j !=0 :
            break
        print(*line_list)


def main():
    n = int(sys.stdin.readline().rstrip())
    line = sys.stdin.readline().rstrip()
    line_list = list(map(int, line.split()))
    bubble_sort(line_list, n)


if __name__ == '__main__':
    main()
