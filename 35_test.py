# Python을 파이썬으로 바꿔라
file = open('C:/pythonEX/txr/python.txt', 'r', encoding='UTF8')

str = file.read()  # 파일 내용을 문자열로 저장함
print(f'파일 내용 : {str}')

str = str.replace('Python', '파이썬', 2)  # 전체가 아니라, 앞의 2개만 바꿔라

file.close()  #반드시 닫기


file = open('C:/pythonEX/txr/python.txt', 'w', encoding='UTF8')
file.write(str)
file.close()  
