'''
문제 1) 왕실의 나이트

1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
입력 예시 : a1
출력 예시 : 2 # 나이트가 이동할 수 있는 경우의 수 출력
'''

import sys
input = sys.stdin.readline
knight = list(input())
x = int(ord(knight[0])) - int(ord('a')) + 1
y = int(knight[1])
steps = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, -1), (2, 1), (-1, -2), (1, -2)]
cnt = 0

for step in steps:
    row = y + step[0]
    col = x + step[1]
    if row >= 1 and row <= 8 and col >= 1 and col <= 8:
        cnt += 1
        
print(cnt)