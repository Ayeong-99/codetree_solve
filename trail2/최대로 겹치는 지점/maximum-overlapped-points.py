n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

arr = [0] * 101

for i in range(n):
    x1, x2 = segments[i]

    for j in range(x1, x2+1):
        arr[j] += 1
    

max_n = max(arr)
print(max_n)
