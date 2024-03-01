n = int(input())
if 1 <= n < 360:
    hours = n // 30
    minutes = n * 2
    print(hours, minutes)