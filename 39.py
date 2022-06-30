'''
readlines() : 파일의 모든 데이터를 읽어서 리스트 형태로 반환
readline() : 한 행을 읽어서 문자열로 반환
'''
'''
# readlines
uri = 'C:/pythonEX/txr/'
with open(uri + 'kk.txt', 'r') as f:
    kk_list = f.readlines()

print(f'kk_list : {kk_list}')  #개행도 읽음
print(f'kk_list type : {type(kk_list)}')
'''
# readline
uri = 'C:/pythonEX/txr/'
with open(uri + 'kk.txt', 'r') as f:
    line = f.readline()

    while line != '':    #한 행만 읽기 때문에 다 읽으려면 반복문 필요
        print(f'line : {line}', end='')
        line = f.readline()
        
