a, b = map(int, input().split())
n = input()

# Please write your code here.

# a 진수를 10진수로 변환

deci_n = 0
for num in n:
    deci_n = deci_n * a + int(num)


deci_to_b = []
while True:
    if deci_n < b:
        deci_to_b.append(deci_n)
        break
    
    deci_to_b.append(deci_n % b)
    deci_n //= b

for i in deci_to_b[::-1]:
    print(i,end="")