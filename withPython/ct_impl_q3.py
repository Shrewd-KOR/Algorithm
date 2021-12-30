# 출처: 동빈나 (이코테 2021 강의 몰아보기) 2. 그리디 & 구현
# 왕실의 나이트

pos = input()
row = int(pos[1])
col = int(ord(pos[0])) - int(ord('a')) + 1

steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]

cnt = 0

for step in steps:
    nrow = row + step[0]
    ncol = col + step[1]
    if nrow >= 1 and nrow <= 8 and ncol >= 1 and ncol <= 8:
        cnt += 1

print(cnt)
