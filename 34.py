'''
텍스트파일 다루기
open() : 파일 열기
read() : 읽기
write() : 쓰기 (덮어쓴다)
close() : 파일 닫기
'''

# 뒤에 'r'은 읽기모드, 'w'는 쓰기모드를 의미
# 'r'인 경우, 파일이 없으면 오류가 난다.
# 'w'인 경우, 파일이 없으면 새로 만든다.
file = open('C:/pythonEX/txr/dd.txt', 'w')

strCnt = file.write('Hello World~')     # 기존 글자를 지우고 새로 쓴다
print(f'쓰여진 문자의 개수(띄어쓰기 포함) : {strCnt}')

file.close()  #반드시 닫기