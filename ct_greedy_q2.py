# 출처: 동빈나 (이코테 2021 강의 몰아보기) 2. 그리디 & 구현
# 02984 => 576
data = input()

result = int(data[0])

for x in range(1,len(data)):
    num = int(data[x])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)   
