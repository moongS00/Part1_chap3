# 객체 복사에 대한 이해
'''
클래스에서 얕은복사와 깊은복사

# 1. 얕은 복사 : 객체 주소를 복사하는 것
import copy


class Tem:

    def __init__(self, n, s):
        self.num = n
        self.str = s

    def info(self):
        print(f'num : {self.num}')
        print(f'str : {self.str}')


a1 = Tem(10, 'H')
a2 = a1

a1.info()
a2.info()

a2.num = 5
a2.str = 'pp'

a1.info()   # a2만 바꿨지만 a1도 바뀜
a2.info()


# 2. 깊은 복사 객체 자체를 복사하는 것 => 또 하나의 객체가 만들어진다
# 깊은 복사를 할 때 copy.copy() 함수를 자주 사용
b1 = Tem(10, ' TT')
b2 = copy.copy(b1)

b1.info()
b2.info()

b2.num = 99
b2.str = 'hi'

b1.info()
b2.info()
'''


'''
리스트에서 얕은복사와 깊은복사
'''
# 1. 얕은복사
li = [9, 8, 5, 7, 6]
copy_li = []

copy_li = li
print(f'id(li) : {id(li)}')
print(f'id(copy_li) : {id(copy_li)}')

# 2. 깊은복사
## 1) for문 & append() 함수
for s in li:
    copy_li.append(s)
print(f'id(li) : {id(li)}')
print(f'id(copy_li) : {id(copy_li)}')

## 2) extend() 함수
copy_li.extend(li)
print(f'id(li) : {id(li)}')
print(f'id(copy_li) : {id(copy_li)}')

## 3) copy() 함수
import copy
copy_li = li.copy()
print(f'id(li) : {id(li)}')
print(f'id(copy_li) : {id(copy_li)}')

## 4) 슬라이스
copy_li = li[:]
print(f'id(li) : {id(li)}')
print(f'id(copy_li) : {id(copy_li)}')
