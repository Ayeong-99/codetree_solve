m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weeks = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days = 0

def cal_day(m, d):
    month = 1
    day = 0
    while month != m:
        day += num_of_days[month]
        month += 1

    day += d
    return day

days = cal_day(m2, d2) - cal_day(m1, d1)
print(weeks[days%7])
