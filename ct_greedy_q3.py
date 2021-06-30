# 출처: 동빈나 (이코테 2021 강의 몰아보기) 2. 그리디 & 구현

N = int(input())

gongpo = input().split()
# gongpo = list(map(int, input().split()))

print(N)
print(gongpo)

gongpo.sort()
print(gongpo)


group = 0
people = 0
for i in range(0,len(gongpo)):
    people += 1
    if int(gongpo[i]) <= people :
        group += 1
        people = 0

print(group)

