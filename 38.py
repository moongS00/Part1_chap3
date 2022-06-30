# 반복 가능한 자료형의 데이터를 파일에 쓸때
# writelines()는 리스트나 튜플을 파일에 쓰기 위한 함수

uri = 'C:/pythonEX/txr/'
lan = ['c', 'java', 'c#', 'python', 'js']
'''
for item in lan:
    with open(uri + 'languages.txt', 'a') as f:
        f.write(item)
        f.write('\n')

아래가 더 쉬운 방법        
'''
with open(uri + 'languages.txt', 'w') as f:
    f.writelines(item + '\n' for item in lan)  # 개행하는 방법