n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.

arr = [0] * n

for i in range(k):
    a, b = commands[i]
    for j in range(a-1, b):
        arr[j] += 1
    
block_max = max(arr)
print(block_max)