# 파일에 저장된 과목별 점수를 파이썬에서 읽어, 딕셔너리에 저장하는 코드를 만들어보자
uri = 'C:/pythonEX/txr/'
scoreDic = {}

with open(uri + 's.txt', 'r') as f:
    line = f.readline()

    while line != '':
        tempList = line.split(':')
        scoreDic[tempList[0]] = int(tempList[1].strip('\n'))

        line = f.readline()

print(f'scoreDic : {scoreDic}')
