N = int(input())
plans = list(input().split())
x, y = 1, 1

for plan in plans:
    if (x > 0 and y > 0 and x <= N and y <= N):
        if plan == 'L' and y > 1:
            y -= 1
        elif plan == 'R':
            y += 1
        elif plan == 'U' and x > 1:
            x -= 1
        elif plan == 'D':
            x += 1
    else: 
        continue

print(x, y)









