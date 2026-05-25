m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = 0

# 1월 1일 부터 m1 d1 까지와 m2 d2 까지 계산해서 빼기
def cal_days(m, d):
    day = 0
    month = 1
    while month != m:
        
        day += num_of_days[month]
        month += 1
    day += d
    return day

days = cal_days(m2, d2) - cal_days(m1, d1) + 1

print(days)