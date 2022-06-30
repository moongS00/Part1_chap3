def cm_mm(n):
    return round(n * 10, 3)

def cm_inch(n):
    return round(n * 0.393, 3)

def cm_M(n):
    return round(n * 0.01, 3)

def cm_ft(n):
    return round(n * 0.032, 3)

if __name__ == '__main__':   #이 파일이 메인 파일인 경우에만 실행된다
    print(f'10cm : {cm_mm(10)}mm')
    print(f'10cm : {cm_inch(10)}inch')
    print(f'10cm : {cm_M(10)}m')
    print(f'10cm : {cm_ft(10)}ft')