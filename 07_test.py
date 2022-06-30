# 계산기 함수를 선언하고 그 안에 덧셈, 뺄셈, 곱셈, 나눗셈 함수를 선언하자

def calculator(n1, n2, operator):
    def add_cal():
        print('덧셈 연산 : %.1f' %(n1+n2))

    def sub_cal():
        print('뺄셈 연산 : %.1f' %(n1-n2))

    def mul_cal():
        print('나눗셈 연산 : %.1f' %(n1/n2))

    def div_cal():
        print('곱셈 연산 : %.1f' %(n1*n2))

    if operator == 1:
        add_cal()
    elif operator == 2:
        sub_cal()
    elif operator == 3:
        mul_cal()
    elif operator == 4:
        div_cal()
    elif operator == 5:
        print('종료')



a1 = float(input('실수(n1) 입력 : '))
a2 = float(input('실수(n2) 입력 : '))
op = int(input('1.덧셈\t2.뺄셈\t3.곱셈\t4.나눗셈\t5.종료\t'))
calculator(a1, a2, op )

#계산기 무한반복 방법
'''
while True:
    num1 = float(input('실수(n1) 입력 : '))
    num2 = float(input('실수(n2) 입력 : '))
    ope = int(input('1.덧셈\t2.뺄셈\t3.곱셈\t4.나눗셈\t5.종료\t'))

    if ope == 5:
        print('Bye~')
        break

    calculator(num1, num2, ope)
'''