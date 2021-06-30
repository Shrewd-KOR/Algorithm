# 출처: 동빈나 (이코테 2021 강의 몰아보기) 2. 그리디 & 구현
# 문자열 재정렬


str1 = input()
str2 = []

sum = 0

for c in str1:
    if c.isalpha():
        str2.append(c)
    else:
        sum += int(c)

str2.sort()

str2.append(str(sum))

print(str2)

print(''.join(str2))
