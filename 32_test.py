# 사용자가 문자를 보낼때 10글자 이하면 SMS로 발송하고
# 10글자를 초과하면 MMS로 발송하는 프로그램을 예외 처리를 이용해서 만들어보자

def sendSMS(msg):

    if len(msg) > 10:
        raise Exception('길이 초과. MMS전환 후 발송', 1)
    else:
        print('SMS 발송')


def sendMMS(msg):

    if len(msg) <= 10:
        raise Exception('길이 미달. SMS전환 후 발송.', 2)
    else:
        print('MMS 발송')


msg = input('input message: ')

try:
    sendSMS(msg)
except Exception as e:
    print(f'exception : {e.args[0]}') 
    print(f'exception : {e.args[1]}')

    if e.args[1] == 1:
        sendMMS(msg)
    elif e.args[1] == 2:
        sendSMS(msg)
