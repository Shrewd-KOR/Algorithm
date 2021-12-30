# 출처: 동빈나 (이코테 2021 강의 몰아보기) 2. 그리디 & 구현
# 완전탐색(Brute Forcing)문제유형

N = int(input())

cnt = 0
for hh in range(N+1):
    for mm in range(60):
        for ss in range(60):
            if '3' in str(hh)+str(mm)+str(ss):
                cnt += 1

print(cnt)
