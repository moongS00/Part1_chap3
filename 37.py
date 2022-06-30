# close 생략 : with~as 문
uri = 'C:/pythonEX/txr/'

with open(uri + 'hello.txt', 'a') as f:
    f.write('python')

with open(uri + 'hello.txt', 'r') as f:
    print(f.read())