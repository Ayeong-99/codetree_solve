binary = input()

# Please write your code here.
num = 0
digit = len(binary)
for i in range(digit):
    num = num * 2 + int(binary[i])

print(num)