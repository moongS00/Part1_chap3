# 선수의 원본 점수를 이용해서 평균을 출력하고,
# 최고값과 최저값을 제회한 평균을 출력하는 프로그램을 만들어보자

ori_score = [8.7, 9.1, 8.9, 9.0, 7.9, 9.5, 8.8, 8.3]
copy_score = ori_score.copy()

ori_score.sort()

copy_score.sort()
copy_score.pop(0)
copy_score.pop()

print(f'원점수 : {ori_score}')
print(f'절사점수 : {copy_score}')

ori_to = round(sum(ori_score), 2)
ori_avg = round(ori_to/len(ori_score), 2)
print(f'원총점 : {ori_to}')
print(f'원평균 : {ori_avg}')

copy_to = round(sum(copy_score), 2)
copy_avg = round(copy_to/len(copy_score), 2)
print(f'절사총점 : {copy_to}')
print(f'절사평균 : {copy_avg}')
print(f'원평균 - 절사평균 : {round((ori_avg- copy_avg),2) }')

