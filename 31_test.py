# 사용자로부터 숫자 5개를 입력받아 짝수, 홀수, 실수와 입력한 모든 데이터를 각각 출력하는 프로그램을 만들어보자

even_List = []; odd_List = []; float_List = []; data_List = []

n = 1

while n < 6:

    try:
        data = input('숫자를 입력하세요 : ')
        num = float(data)
    except:
        print('문자입니다. 숫자를 입력하세요.')
        continue
    else:
        if num - int(num) != 0:
            float_List.append(num)

        else:
            if num % 2 == 0:
                even_List.append(int(num))

            else:
                odd_List.append(int(num))

        n += 1
    finally:
        data_List.append(data)

print(f'even_List : {even_List}')
print(f'odd_List  : {odd_List}')
print(f'float_List : {float_List}')
print(f'data_List : {data_List}')