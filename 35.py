# 텍스트파일 읽기
file = open('C:/pythonEX/txr/diary.txt', 'r')

str = file.read()  # 파일 내용을 문자열로 저장함
print(f'파일 내용 : {str}')

file.close()  #반드시 닫기


