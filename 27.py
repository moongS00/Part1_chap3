'''
추상클래스
상속관계에서
상위 클래스가 하위 클래스에게 매서드 구체화를 강요하는것

그러기 위해서는 아래와 같은 abc어쩌구 모듈을 사용해서 강제성을 부여해야 한다

특정 기능을 상속받은 클래스마다 다르게 사용할 수 있도록 하는 기능이라나 뭐라나
'''

from abc import ABCMeta
from abc import abstractmethod

class AirPlane(metaclass=ABCMeta):

    @abstractclassmethod
    def flight(self):
        pass

    def forward(self):
        print('전진!')

    def backward(self):
        print('후진!')


class Airliner(AirPlane):
    def flight(self):
        print('시속 400km/h 비행!!')


class FightPlane(AirPlane):
    def flight(self):
        print('시속 900km/h 비행!!')


m = Airliner()
m.flight()
m.forward()
m.backward()

k = FightPlane()