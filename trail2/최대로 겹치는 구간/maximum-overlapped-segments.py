n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
arr = [0] * 201

for i in range(n):
    x1, x2 = segments[i]
    x1 += 100
    x2 += 100
    for j in range(x1, x2):
        arr[j] += 1
    

max_n = max(arr)
print(max_n)