# 다중 상속
class Car1:
    def drive(self):
        print('drive() called!')


class Car2:
    def back(self):
        print('back() called!')


class Car3:
    def turbo(self):
        print('turbo() called!')


class Car(Car1, Car2, Car3):
    def __init__(self):
        pass


my = Car()

my.turbo()
my.back()
my.drive()
