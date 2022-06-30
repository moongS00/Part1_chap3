# 로또번호 생성기 프로그램을 만들고 파일에 번호를 출력해보자
import random
uri = 'C:/pythonEX/txr/'

def lottery(nums):
    for idx, num in enumerate(nums):
        with open(uri + 'lottery.txt', 'a') as f:
            if idx < (len(nums) - 2):
                f.write(str(num) + ', ')
            elif idx == (len(nums) - 2):
                f.write(str(num))
            elif idx == (len(nums) - 1):
                f.write('\n')
                f.write('bonus: ' + str(num))
                f.write('\n')


rnums = random.sample(range(1,46),7)
print(f'번호 : {rnums}')

lottery(rnums)



