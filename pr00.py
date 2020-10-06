import sys
input = lambda: sys.stdin.readline().rstrip()

a = list(map(int,input().split()))

if all(x<y for x,y in zip(a[:-1],a[1:])):
    print("ascending")
elif all(x>y for x,y in zip(a[:-1],a[1:])):
    print("descending")
else:
    print("mixed")
