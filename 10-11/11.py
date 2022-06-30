#모듈을 사용하는 다양한 방법

#1. impor 사용 : 전 시간에 사용한 방법
import calculator
calculator.add(10, 20)

#2. as키워드를 이용
import calculator as cal
cal.add(10,20)

#3. from~as키워드를 이용해서 모듈의 특정 기능만 사용 가능
from calculator import *   #calculator모듈의 모든 기능을 가져오는 방법
sub(50,30)
mul(2,4)  #from키워드로 가졍ㄴ 경우엔 모듈명을 적지 않고도 기능에 접근할 수 있다

