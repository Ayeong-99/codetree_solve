N = int(input())

command = []
num = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push_back" or line[0] == "get":
        num.append(int(line[1]))
    else:
        num.append(0)

# Please write your code here.
arr = []
size = 0
for i in range(N):
    now_command = command[i]
    if now_command == "push_back":
        arr.append(num[i])
        size += 1 
    elif now_command == "pop_back":
        arr.pop()
        size -= 1
    elif now_command == "size":
        print(size)
    elif now_command == "get":
        geti = num[i] - 1
        print(arr[geti])