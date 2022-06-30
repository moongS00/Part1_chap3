# 텍스트 파일 열기
'''
<파일 모드>
파일 모드는 파일을 어떤 목적으로 open할지 정한다
'w' : 쓰기 전용 (내용 있으면 덮어씌움)
'a' : 쓰기 전용 (내용 있으면 덧붙임)
'x' : 쓰기 전용 (파일 있으면 에러발생)
'r' : 읽기 전용 (파일 없으면 에러발생)
'''

# 'w' 모드
file = open('C:/pythonEX/txr/hello.txt', 'w')
file.write('Hello World~')
file.close()

# 'a' 모드
file = open('C:/pythonEX/txr/hello.txt', 'a')
file.write('\nNice!!')
file.close()

# 'x' 모드
file = open('C:/pythonEX/txr/hello2.txt', 'x')
file.write('\nNice!!')
file.close()

# 'r' 모드
file = open('C:/pythonEX/txr/hello2.txt', 'r')
str = file.read()
print(f'파일 내용 : {str}')
file.close()
