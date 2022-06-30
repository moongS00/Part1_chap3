# 딕셔너리에 저장된 과목별 점수를 파일에 저장하는 코드를 작성하자

scoreDic = {'kor':85, 'eng':90, "mat":92, 'sci': 79, 'his': 82}

uri = 'C:/pythonEX/txr/'
for key in scoreDic.keys():
    with open(uri + 'scoreDic.txt', 'a') as f:
        f.write(key + '\t:\t' + str(scoreDic[key]) + '\n')

with open(uri + 'scores.txt', 'a') as f:
    print(scoreDic, file=f)   #딕셔너리,리스트 모양 그대로 파일에 저장하는 방법