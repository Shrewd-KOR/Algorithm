# 출처: 동빈나 (이코테 2021 강의 몰아보기) 2. 그리디 & 구현

N = int(input())
plan = input().split()

#    동  북  서  남
dx = (0, -1, 0, 1)
dy = (1, 0, -1, 0)

x = 1
y = 1

for i in plan:
    if i == 'R':
        nx = x + dx[0]
        ny = y + dy[0]
    elif i == 'U':
        nx = x + dx[1]
        ny = y + dy[1]        
    elif i == 'L':
        nx = x + dx[2]
        ny = y + dy[2]
    elif i == 'D':
        nx = x + dx[3]
        ny = y + dy[3]
    else:
        pass
    
    if(nx < 1 or nx > N or ny < 1 or ny > N):
        continue
    else:
        x = nx
        y = ny

print(x,y)        