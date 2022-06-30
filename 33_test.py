# 관리자 암호를 입력하고 상태에 따라 예외 처리하는 예외 클래스를 만들어보자

class PasswordLengthShortException(Exception):
    def __init__(self, str):
        super().__init__(f'{str}: 길이 5 미만!')


class PasswordLengthLongException(Exception):
    def __init__(self, str):
        super().__init__(f'{str}: 길이 10 초과!')


class PasswordWrongException(Exception):
    def __init__(self, str):
        super().__init__(f'{str}: 잘못된 비밀번호!')


flag = True

while flag:
    try:
        adminpw = input('input admin password: ')
        if len(adminpw) < 5:
            raise PasswordLengthShortException(adminpw)

        elif len(adminpw) > 10:
            raise PasswordLengthLongException(adminpw)

        elif adminpw != 'admin1234':
            raise PasswordWrongException(adminpw)

        elif adminpw == 'admin1234':
            print('빙고!')
            flag = False

    except PasswordLengthShortException as e1:
        print(e1)
        continue

    except PasswordLengthLongException as e2:
        print(e2)

    except PasswordWrongException as e3:
        print(e3)



