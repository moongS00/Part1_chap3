# 시스템 시간과 일정을 텍스트 파일에 작성해보자
import time

lt = time.localtime()
#datestr = '[' + str(lt.tm_year) + '년 ' + \
#          str(lt.tm_mon) + '월 ' + str(lt.tm_mday) + '일' + ']'

datestr = '[' + time.strftime('%Y-%m-%d %I:%M:%S %p') + ']'
# 대소문자 구별하기(m은 원, M은 분) (H는 24시간, I는 오전9시, 오후9시 이런식)
# p는 am/pm을 의미

diary = input('오늘 일정 : ')

file = open('C:/pythonEX/txr/diary.txt', 'w')
file.write(datestr + diary)
file.close()  #반드시 닫기