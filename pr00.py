import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
c_0 = [1,0,1]
c_1 = [0,1,1]
def fib(chk):
    if len(c_0) <= chk:
        for i in range(len(c_0),chk+1):
            c_0.append(c_0[i-1] +c_0[i-2])
            c_1.append(c_1[i-1] +c_1[i-2])

    print(c_0[chk],c_1[chk])
            

for _ in range(n):

    chk = int(input())

    fib(chk)

