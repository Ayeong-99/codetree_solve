N = input()

# Please write your code here.

deci = 0
for s in N:
    deci = deci * 2 + int(s)


deci_mult17 = deci * 17

digits = []
while True:
    if deci_mult17 < 2:
        digits.append(deci_mult17)
        break

    digits.append(deci_mult17 % 2)
    deci_mult17 //= 2

for digit in digits[::-1]:
    print(digit, end="")
