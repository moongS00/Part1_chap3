#삼각형, 사각형, 원의 넓이를 반환하는 lamda함수를 만들어보자

tri_area = lambda n1, n2 : n1 * n2 / 2
sqa_area = lambda n1, n2 : n1 * n2
cir_area = lambda r : r * r * 3.14

w = int(input('가로 길이 입력 : '))
h = int(input('세로 길이 입력 : '))
r = int(input('반지름 길이 입력 : '))

tri = tri_area(w,h)
sqa = sqa_area(w,h)
cir = cir_area(r)

print(f'삼각형 넓이 : {tri}')
print(f'사각형 넓이 : {sqa}')
print(f'원 넓이 : {cir}')