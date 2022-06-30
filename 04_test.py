#국어, 영어, 수학점수를 입력받고 총점과 평균을 출력하는 함수를 만들어보자
def printScore(kor, eng, mat):
    sum = kor + eng + mat
    avg = sum / 3

    print('총점: {}'.format(sum))
    print('평균: %.2f' %avg)

kor_score = int(input('국어 점수 입력 : '))
eng_score = int(input('영어 점수 입력 : '))
mat_score = int(input('수학 점수 입력 : '))

printScore(kor_score, eng_score, mat_score)