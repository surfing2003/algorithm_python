import sys
input = lambda : sys.stdin.readline().rstrip()


def hanoi(n, before, after, temp):
    if n == 1:
        print(before, after)
        return
    hanoi(n-1,before,temp,after)
    print(before, after)
    hanoi(n-1,temp,after,before)

N = int(input())
print((2**N) -1)
hanoi(N,1,3,2)
