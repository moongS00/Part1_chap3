import random

#1. random모듈을 이용해 1부터 10까지의 정수 중 난수 1개를 발생시켜보자
r_num = random.randint(1,10)
print(r_num)

#2. random모듈을 이용해 1부터 100까지의 정수 중 난수 10개를 발생시켜보자
r_num2 = random.sample(range(1, 101), 10)
print(r_num2)