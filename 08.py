'''
lamda 키워드를 이용하면
함수 선언을 보다 간단하게 할 수 있다
'''

#-----일반적인 방법-----
def cal(n1, n2):
    return n1 + n2

re_val = cal(10 , 20)
print(f'return : {re_val}')


#-----lamda 방법-----
cals = lambda a1, a2 : a1 + a2
res = cals(3,8)
print(f'return : {res}')
