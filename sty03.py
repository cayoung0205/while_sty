## 고무 공을 100m 높이에서 떨어뜨림
## 공은 땅에 닿을 때마다 원래 높이의 3/5만큼 튀어오름
## 10번 반복한 후 높이 계산
# round(수, 자리) : 자리로 반올림

heigh=100
bounce = 3/5

n=1

while n<=10:
    heigh=heigh*bounce
    print(n, round(heigh,4))
    n += 1