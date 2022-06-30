#1. 사용자가 가로, 세로 길이를 입력하면 삼각형과 사각형의 넓이를 출력하는 함수를 만들어보자

width = int(input('가로 길이 입력 : '))
height = int(input('세로 길이 입력 : '))

def area():
    tri = width * height / 2
    sqa = width * height

    print('삼각형 넓이 : {}'.format(tri))
    print('사각형 넓이 : {}'.format(sqa))

area()


#2. qkdansror tnfmf zkdnsxmgksms gkatnfmf aksemfdjqhwk
total_visit = 0
def count():
    global total_visit

    total_visit += 1
    print('누적 방문객 : {}'.format(total_visit))

count()
count()
count()
count()
count()