N, B = map(int, input().split())

# Please write your code here.


num = []
while  N != 0: # 몫이 0이 아닐때 까지 계속 진행
    left = N % B
    num.append(left)
    N = N // B

last = len(num)-1
for i in range(last, -1, -1):
    print(num[i], end="")