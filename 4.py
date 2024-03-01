x, y, n = map(int, input().split())
kopecks = x * 100 + y
income = kopecks * n
print(f'{income // 100} руб. {income % 100} коп.')