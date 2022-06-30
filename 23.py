# 생성자
# 객체가 생성될 때 생성자를 호출하면 __init__()가 자동 호출된다
class Cal:

    def __init__(self):
        print('[Cal] __init__() called!')


cal = Cal()  # Cal()생성자 호출 -> Cal의 __init__() 호출


# super() : 상위 클래스의 속성을 초기화하기 위해 사용
class P_class:

    def __init__(self, pnum1, pnum2):
        print('[P_class] __init__()')
        self.pnum1 = pnum1
        self.pnum2 = pnum2


class C_class(P_class):

    def __init__(self, cnum1, cnum2):
        print('[C_class] __init__()')

        super().__init__(cnum1, cnum2)  # 기능은 상속만 하면 바로 사용가능하지만 속성은 init메소드로 초기화를 해줘야 사용할 수 있다

        self.cnum1 = cnum1
        self.cnum2 = cnum2


k = C_class(1, 2)