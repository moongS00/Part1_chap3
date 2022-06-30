# 과목별 점수를 입력받아 리스트에 저장하고 원본을 유지한 상태로,
# 복사본을 만들어 과목별 점수를 10%올렸을 경우에 평균을 출력해보자

scores = [int(input('국어 점수 입력 : ')),
          int(input('영어 점수 입력 : ')),
          int(input('수학 점수 입력 : '))]

print(scores)

copy_scores = scores.copy()    # 아까와 달리, 객체 자체를 복사

for idx, score in enumerate(copy_scores):
    res = score * 1.1
    print('인덱스는 {} 이고 점수는 {} 이다'.format(idx, score))
    copy_scores[idx] = 100 if res > 100 else res

print(f'이전 평균 : {sum(scores) / len(scores)}')
print(f'이후 평균 : {sum(copy_scores) / len(copy_scores)}')

'''
enumerate() :
리스트의 인덱스를 자동 생성해주는 함수
idx는 인덱스, score은 입력된 점수를 의미
'''