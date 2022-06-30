# 클래스 상속
class NormalCar:

    def drive(self):
        print('[NormalCar] drive() called!')

    def back(self):
        print('[NormalCar] back() called!')


class TurboCar(NormalCar):

    def turbo(self):
        print('[TurboCar] turbo() called!')
'''
class TurboCar(NormalCar):
클래스 작성시 괄호 안에 넣으면
괄호 안에 있는 클래스를 상속받을 수 있다
'''

a = TurboCar()
a.turbo()
a.drive()
a.back()