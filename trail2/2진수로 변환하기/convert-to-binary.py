n = int(input())

# Please write your code here.

solv = ""

while True:
    if n < 2:
        solv = str(n) + solv
        break
    
    solv = str(n % 2) + solv
    n //= 2

print(solv)
