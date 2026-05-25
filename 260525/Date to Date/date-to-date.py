m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = 0

if m1 == m2: # 달이 같은 경우
    days = d2 - d1 + 1
else:
    # 달이 다른 경우 
    # 첫달 일 수 계산
    days += num_of_days[m1] - d1 + 1

    # 첫달 다음달 부터 계산
    m = m1 + 1

    # 막달이랑 달이 같으면 해당 달의 전체 일수는 더하면 안되니까 그 전까지만 더하도록 
    while m != m2:
        days += num_of_days[m]
        m += 1
    days += d2

print(days)



