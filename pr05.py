# N = int(input())

# for i in range(N):
#     print(' '*(i)+'*'*(N-i))

# N = int(input())

# for i in range(N):
#     print(' '*(N-i-1)+'*'*((2*i)+1))


# N = int(input())

# for i in range(N,0,-1):
#     print(' '*(N-i)+'*'*((2*i)-1))

# N = int(input())

# for i in range(N):
#     print(' '*i+'*'*((2*(N-i))-1))

# N = int(input())

# for i in range(N):
#     print(' '*(N-i-1)+'*'*((2*i)+1))

# for i in range(1,N):
#     print(' '*i+'*'*((2*(N-i))-1))

# N = int(input())

# for i in range(1,N):
#     temp = '*'*i + ' '*(N-i)
#     print(temp+temp[::-1])
# for i in range(N,0,-1):
#     temp = '*'*i + ' '*(N-i)
#     print(temp+temp[::-1])

# N = int(input())

# for i in range(1,N):
#     print('*'*i+' '*(2*N-i*2)+'*'*i)
# for i in range(N,0,-1):
#     print('*'*i+' '*(2*N-i*2)+'*'*i)

# N = int(input())

# for i in range(N):
#     print(' '*i+'*'*(2*(N-i)-1))
# for i in range(N-2,-1,-1):
#     print(' '*i+'*'*(2*(N-i)-1))

# N = int(input())
# for i in range(-N+1,N):
#     print(i)
#     print(' '*(N-abs(i)-1) + '*'*(2*abs(i)+1))

################# 시간복잡도 확인
# 752ms
# N, M = map(int,input().split())
# num = 1
# for _ in range(N):
#     for _ in range(M):
#         if num % M == 0:
#             print(num,end = '')
#         else:
#             print(num,end = ' ')
#         num += 1
#     print()

# 556ms
# N,M = map(int,input().split())

# for i in range(N):
#     print(*[ M*i+j+1 for j in range(M)])

# 308ms
# n, m = map(int, input().split())
# for i in range(1, 1 + n*m, m):
#     print(' '.join(map(str, range(i, i+m))))
####################################################

print("       _.-;;-._")
print("'-..-'|   ||   |")
print("'-..-'|_.-;;-._|")
print("'-..-'|   ||   |")
print("'-..-'|_.-''-._|")

print("    8888888888  888    88888")
print("   88     88   88 88   88  88")
print("    8888  88  88   88  88888")
print("       88 88 888888888 88   88")
print("88888888  88 88     88 88    888888")
print("")
print("88  88  88   888    88888    888888")
print("88  88  88  88 88   88  88  88")
print("88 8888 88 88   88  88888    8888")
print(" 888  888 888888888 88  88      88")
print("  88  88  88     88 88   88888888")

print(".  .   .")
print("|  | _ | _. _ ._ _  _")
print("|/\|(/.|(_.(_)[ | )(/.")

print("     /~\\")
print("    ( oo|")
print("    _\\=/_")
print("   /  _  \\")
print("  //|/.\\|\\\\")
print(" ||  \\ /  ||")
print("============")
print("|          |")
print("|          |")
print("|          |")

print("SHIP NAME      CLASS          DEPLOYMENT IN SERVICE")
print("N2 Bomber      Heavy Fighter  Limited    21        ")
print("J-Type 327     Light Combat   Unlimited  1         ")
print("NX Cruiser     Medium Fighter Limited    18        ")
print("N1 Starfighter Medium Fighter Unlimited  25        ")
print("Royal Cruiser  Light Combat   Limited    4         ")

print("NFC West       W   L  T")
print("-----------------------")
print("Seattle        13  3  0")
print("San Francisco  12  4  0")
print("Arizona        10  6  0")
print("St. Louis      7   9  0")
print()
print("NFC North      W   L  T")
print("-----------------------")
print("Green Bay      8   7  1")
print("Chicago        8   8  0")
print("Detroit        7   9  0")
print("Minnesota      5  10  1")