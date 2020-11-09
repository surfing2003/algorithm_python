
import sys
input = lambda : sys.stdin.readline().rstrip()

# 17142 17779 17837 19236 19237 19238
# 17142 17837 다시풀어보기
# 삼성 2072


n = 10
data = [1,8,6,4,2,10,7,5,9,3]
print("정렬전",data)
def quick(start,end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and data[left] <= data[pivot]:
            print("left:",left,data[left],data[pivot])
            left += 1
        while right > start and data[right] >= data[pivot]:
            print("right:",right,data[right],data[pivot])
            right -= 1
        if left > right:
            data[right], data[pivot] = data[pivot], data[right]
            print("l>r",left,right,pivot,data[right],data[pivot])
        else:
            data[left], data[right] = data[right], data[left]
            print("l<=r",data[left],data[right])
    quick(start,right-1)
    quick(right+1,end)
    
quick(0,n-1)
print("정렬후",data)
