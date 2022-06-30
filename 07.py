# 중첩함수 : 함수 안에 또다른 함수가 있는 형태

def out_func():
    print('out func called!')

    def in_func():
        print('in func called!')

    in_func()


out_func()
#in_func()  #내부 함수는 외부함수 밖에서 호출할수 없다