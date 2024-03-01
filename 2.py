time = int(input())
if 1 <= time < 86400:
    hours = time //3600
    minutes = time % 3600 // 60
    seconds = time % 60
    print(hours, minutes, seconds, sep=':')